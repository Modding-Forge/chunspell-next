import os
import platform
import sys
from collections import defaultdict
from distutils.command.build import build

from setuptools import Extension, setup
from setuptools.command.bdist_wheel import bdist_wheel as _bdist_wheel
from setuptools.command.build_ext import build_ext

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from build_hunspell import pkgconfig, repair_darwin_link_dep_path


class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        _bdist_wheel.finalize_options(self)
        # Mark us as not a pure Python package.
        self.root_is_pure = False


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BUILD_ARGS = defaultdict(lambda: ['-O3', '-g0'])
for compiler, args in [
        ('msvc', ['/EHsc', '/MD', '/DHUNSPELL_STATIC']),
        ('gcc', ['-O3', '-g0', '-DHUNSPELL_STATIC'])]:
    BUILD_ARGS[compiler] = args


def cleanup_pycs():
    file_tree = os.walk(os.path.join(BASE_DIR, 'hunspell'))
    to_delete = []
    for root, directory, file_list in file_tree:
        if len(file_list):
            for file_name in file_list:
                if file_name.endswith('.pyc'):
                    to_delete.append(os.path.join(root, file_name))
    for file_path in to_delete:
        try:
            os.remove(file_path)
        except OSError:
            pass


class build_ext_compiler_check(build_ext):
    def build_extensions(self):
        native_config = pkgconfig()
        compiler = self.compiler.compiler_type
        args = BUILD_ARGS[compiler]
        for ext in self.extensions:
            for key, value in native_config.items():
                setattr(ext, key, value)
            ext.extra_compile_args = args
        build_ext.build_extensions(self)

    def run(self):
        cleanup_pycs()
        build_ext.run(self)


class build_darwin_fix(build):
    def run(self):
        build.run(self)
        # macOS builds a shared dependency with an absolute path to the
        # Hunspell dylib. Repair it to use the loader-relative path.
        if platform.system() == 'Darwin':
            repair_darwin_link_dep_path()


setup(
    ext_modules=[
        Extension(
            'hunspell.hunspell',
            [os.path.join('hunspell', 'hunspell.cpp')],
            language='c++',
        )
    ],
    cmdclass={
        'build_ext': build_ext_compiler_check,
        'build': build_darwin_fix,
        'bdist_wheel': bdist_wheel,
    },
)
