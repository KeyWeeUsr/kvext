# kvext

KV language extensions

Similar to C macros, KV language can also set up functions with its
``#:set`` directive. That directive uses ``eval()``, which allows a user
to use it even in a dirty way such as extending the original functionality
of the language with own built-ins e.g. for loops or widget swapping.

### Install

* Copy or clone to your app folder
* Include it in your ``.kv`` file with `#:include``
