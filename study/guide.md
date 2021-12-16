Module 1: Browser Architecture (General, Chrome, Safari/Webkit)

- Breaking down modern browser architectures, major components
    - [inside modern browser, google](https://developers.google.com/web/updates/2018/09/inside-browser-part1])
- Setting up a browser research environment, building, debugging
    - [setting up v8 in a vm]
- Interfacing with different components of the browser (DOM, JS)
- Introduction to JavaScript engines
    - [gitconnected](https://levelup.gitconnected.com/inside-the-javascript-engine-896c64cb7623)
    - note: js is a compiled language
    - todo: debug console.log

- A deep-dive into JavaScript engine internals
    - [hidden classes](https://richardartoul.github.io/jekyll/update/2015/04/26/hidden-classes.html)
    - [java objects in memory](https://www.programcreek.com/2011/11/what-do-java-objects-look-like-in-memory/)
    - [link from google](https://mathiasbynens.be/notes/shapes-ics)
- Low-level JavaScript types and natives
    - [mozilla js data objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
    - [garbage collector](https://v8.dev/blog/trash-talk)

Module 2: JavaScript Internals in Exploitation (General, V8, JSC)

- Garbage collection implementations
- Current vulnerability patterns found in JS engines
- Introduction to exploit building blocks (Primitives)
- Leveraging JavaScript vulnerability classes
- Layering exploit primitives

Module 3: JavaScript JIT Compilers (General, V8)

- Overview of JavaScript JIT compiler pipelines
- Exploring JIT debugging tools
- Optimizations and typing
- Type cache and speculation
- JIT vulnerability classes, contemporary exploits

Module 4: JavaScript Exploit Engineering (General, V8, JSC)

- Constructing arbitrary memory primitives
- Overwriting JIT structures and control flow hijacking
- Continuation of execution
- Bypassing browser-specific mitigations
- UXSS, SOP bypasses, and renderer-only attacks
- N-Day exploitation

More good stuff:
[project zero dom fuzzing](https://googleprojectzero.blogspot.com/2018/10/365-days-later-finding-and-exploiting.html) try using this on an random browser

[fuzzing project](https://hexgolems.com/2019/12/hotfuzz/)