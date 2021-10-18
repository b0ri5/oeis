# See https://docs.bazel.build/versions/master/build-ref.html#workspace
workspace(
    name = "wksp",
    managed_directories = {"@npm": ["node_modules"]},
)

# Make Go rules available. See https://github.com/bazelbuild/rules_go#initial-project-setup
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
# Make python rules available. See https://github.com/bazelbuild/rules_python#getting-started
http_archive(
    name = "rules_python",
    sha256 = "954aa89b491be4a083304a2cb838019c8b8c3720a7abb9c4cb81ac7a24230cea",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.4.0/rules_python-0.4.0.tar.gz",
)
