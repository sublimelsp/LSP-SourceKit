# LSP-SourceKit

This is a helper package that automatically configures
[Apple's SourceKit](https://github.com/apple/sourcekit-lsp) language server for
you.

To use this package, you must have:
- A Mac.
- The [LSP](https://packagecontrol.io/packages/LSP) package.
- Xcode and/or its command-line tools.

## Applicable Selectors

This language server operates on views with base scopes:
- `source.swift` (Swift files),
- `source.c` (C files),
- `source.c++` (C++ files),
- `source.objc` (Objective-C files),
- `source.objc++` (Objective-C++ files)

## Installation Location

Nothing is installed. The plugin will use the language server bundled with Xcode.

## Configuration

Configure SourceKit by accessing `Preferences > Package Settings > LSP > Servers > LSP-SourceKit`.
