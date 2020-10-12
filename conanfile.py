from conans import ConanFile, CMake, tools


class JuceconanConan(ConanFile):
    name = "juce"
    version = "0.1"
    license = "GPL3"
    author = "Izmar Verhage, izmaelverhage@gmail.com"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "conan wrapper for JUCE6"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def source(self):
        self.run("git clone https://github.com/juce-framework/JUCE .")
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["juce"]

