# Compiled Markup Language

## ⚠ **WARNING** ⚠
**THIS LANGUAGE IS STILL UNDER *HEAVY* DEVELOPMENT**
# 
**Compiled Markup Language** or **CML** is a markup language that aims to ease the creation of **HTML documents**. Every `.cml` file is compiled into a fully working `index.html` file with all of the content specified inside of the main source file.

### **An Example**
This is an example of how a `.cml` file is structed.

    body <
        header this-is-a-class <
            div Another-Class <
                h1 < 
                    "This is some text"
                >
            >
        >
    >

**CML** replaced the need for closing tags. Making it faster to code with. You need half as much code!

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
