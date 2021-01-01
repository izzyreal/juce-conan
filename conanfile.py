from conans import ConanFile, CMake, tools


class JuceConan(ConanFile):
    name = "juce"
    version = "0.1"
    license = "GPL3"
    author = "Raw Material Software Limited"
    url = "https://github.com/juce-framework/JUCE"
    description = "Open-source cross-platform C++ application framework for desktop and mobile applications"
    topics = ("audio", "music", "dsp", "gui", "cross-platform" )
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def source(self):
        self.run("git clone https://github.com/izzyreal/JUCE .")
        self.run("git checkout raw-keycode")
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        cmake.patch_config_paths()

# Use juce_add_plugin to link the right libs in your consumer
    def package_info(self):
        self.cpp_info.libs = []
