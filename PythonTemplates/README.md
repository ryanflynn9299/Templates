#Python Templates Repository
/github/pipenv/locked/python-version/:user/:repo 

This is a _fairly small_ repo filled with commonly used **Python** snippets.

Since its a ~~boilerplate~~ template repo, this README.md is also a template

That's why there are random things like headings...
## Heading 2
### Heading 3
#### Heading 4

and quotes...
> A line a day keeps the exceptions away! &copy;
(Not really)

and even links! This is definitely not a [Rick Roll](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

I even threw in this cool car to demonstrate images!
![coolImage](https://images.unsplash.com/photo-1639927072187-3cbf34d12f27?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=900&q=60)

But in reality this is still meant for code, so how do you code anyway?

Here's a start:
```
def main():
    println("Hello World!")
```

Incidentally, you run this code like you run the code in the templates.
Each file has a `if __name__ == "__main__":` which is the start to python scripts.
Any code under it like `main()`, will trigger code to run when the script is called from
a run configuration or from the command line (`python <scriptname>.py [args]`)

Here is also an example of a Table:

| first | second | Boolean |
|-------|--------|---------|
| Hello | World  | True    |

and an example of a List:

1. List item 1
2. List item 2
   1. sub item one
   * unordered item 1

Here is a task list:

- [ ] Learn how to code
- [ ] Learn how to make a README
- [x] Exist

If you want to separate out sections, create a line:

---

Or like this:
***

Or even like this:

Header text
=
=============================

subheader text
---
---

To display the following characters:
* \*
* \#
* \+
* \[ ]
* etc

You need to 'escape' them with a \ character (which incidentally does not need to be escaped).

That's all for now folks!
=
