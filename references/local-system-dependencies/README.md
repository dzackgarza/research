# Local System Dependencies

The source directory `~/research-code` contained `mylibs/libflint.so.22`, a symlink to
`/usr/lib/libflint.so.21`.

That symlink was not imported because it points at machine-local system state. Recreate
the dependency through the system package manager or a project environment instead of
tracking the symlink in Git.

