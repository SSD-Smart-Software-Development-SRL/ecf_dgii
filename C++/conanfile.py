from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy
import os


class EcfDgiiClientConan(ConanFile):
    name = "ecf-dgii-client"
    version = "0.1.0"
    license = "MIT"
    author = "Puntoos"
    url = "https://github.com/puntoos/ecf_dgii_clients"
    description = "C++ SDK client for the ECF DGII API (Electronic Fiscal Receipt - Dominican Republic)"
    topics = ("ecf", "dgii", "dominican-republic", "electronic-invoice", "fiscal", "api-client")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
    }
    exports_sources = "CMakeLists.txt", "Config.cmake.in", "include/*", "src/*", "LICENSE"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def requirements(self):
        self.requires("cpprestsdk/2.10.19")
        self.requires("boost/1.86.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["ecf-dgii-client"]
        self.cpp_info.set_property("cmake_file_name", "ecf-dgii-client")
        self.cpp_info.set_property("cmake_target_name", "ecf-dgii-client::ecf-dgii-client")
        self.cpp_info.requires = ["cpprestsdk::cpprest", "boost::headers"]
