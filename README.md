# Compiled Markup Language

## ⚠ **WARNING** ⚠
**THIS LANGUAGE IS STILL UNDER *HEAVY* DEVELOPMENT**

# 
**Compiled Markup Language** or **CML** is a language that aims to ease the creation of HTML documents. Every `.cml` file is compiled into a fully working `index.html` file with all of the content specified inside of the main source file.


### **An Example**
This is an example of how a `.cml` file is structed.

    body 
        header this-is-a-class
            div Another-Class
                h1 "This is some text"

**CML** uses indentation as a way to tell where a tag ends and where it should be placed.

### **After Compilation**:

```html
<body>
    <header class="this-is-a-class">
        <div class="Another-Class">
            <h1>This is some text</h1>
        </div>
    </header>
</body>
```