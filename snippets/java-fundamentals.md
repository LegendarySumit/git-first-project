<div align="center">

# ☕ Java Fundamentals — Code Examples & Concepts

**Practical examples demonstrating core Java concepts**

![Java](https://img.shields.io/badge/Java-007396?logo=java&logoColor=white)
![Learning](https://img.shields.io/badge/Type-Reference-blue)

*From basic structure to variables and I/O*

</div>

---

## 1️⃣ Basic Java Program Structure
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

### Key Understanding

| Keyword | Purpose |
|---------|---------|
| `public` | JVM can access the method |
| `static` | No object needed to run |
| `void` | No return value |
| `main` | Entry point |
| `String[] args` | Command-line arguments |

---

## 2️⃣ Creating a Scanner Object
```java
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter your name:");
        String name = sc.next();

        System.out.println("Hello " + name);
    }
}
```

### Why This Matters

- `Scanner` reads input from `System.in`
- `new` creates an object in memory
- `sc` is a reference variable

---

## 3️⃣ Using `next()` to Read Tokens
```java
Scanner sc = new Scanner(System.in);

String word = sc.next(); // reads one word only
System.out.println(word);
```

### 📌 Important

- `next()` stops at whitespace
- It does **not** read full sentences

---

## 4️⃣ Difference Between System.out, System.in, System.err
```java
System.out.println("This is normal output");

System.err.println("This is an error message");
```

### Stream Purpose

| Stream | Purpose |
|--------|---------|
| `System.in` | Input stream (keyboard) |
| `System.out` | Output stream (console) |
| `System.err` | Error/debug output |

---

## 5️⃣ Type Casting (Widening & Narrowing)

### Implicit (Widening) Casting
```java
int num = 10;
double result = num;

System.out.println(result); // 10.0
```

✅ **Safe** • ✅ **Automatic**

### Explicit (Narrowing) Casting
```java
double value = 9.8;
int number = (int) value;

System.out.println(number); // 9
```

⚠️ **Data loss possible** • ⚠️ **Manual cast required**

---

## 6️⃣ Local Variable Example
```java
public class LocalVar {
    public static void main(String[] args) {
        int x = 10; // local variable
        System.out.println(x);
    }
}
```

### Characteristics

- Exists only inside the method
- Must be initialized before use
- Destroyed after method execution

---

## 7️⃣ Instance Variable Example
```java
public class Student {
    int rollNumber; // instance variable

    void display() {
        System.out.println(rollNumber);
    }
}
```

### Characteristics

- Belongs to the object
- Each object gets its own copy
- Default value assigned if not initialized

---

## 8️⃣ Static Variable Example
```java
public class Counter {
    static int count = 0;

    Counter() {
        count++;
        System.out.println(count);
    }

    public static void main(String[] args) {
        new Counter();
        new Counter();
        new Counter();
    }
}
```

### Output
```
1
2
3
```

### Characteristics

- Shared across all objects
- Memory efficient
- Belongs to the class, not instances

---

## 9️⃣ Local vs Instance vs Static (Quick Comparison)
```java
public class Demo {
    static int s = 10;   // static variable
    int i = 20;          // instance variable

    void show() {
        int l = 30;      // local variable
        System.out.println(s + " " + i + " " + l);
    }
}
```

### Comparison Table

| Type | Scope | Memory | Initialization |
|------|-------|--------|----------------|
| **Local** | Method/Block | Stack | Required |
| **Instance** | Object | Heap | Optional (default values) |
| **Static** | Class | Method Area | Optional (default values) |

---

## 🔑 Key Exam Takeaways

### Input/Output
- ✅ `Scanner` works on input streams
- ✅ `next()` reads tokens, not lines
- ✅ `System.err` is for error messages

### Variables
- ✅ **Local variables** → method scope
- ✅ **Instance variables** → object scope
- ✅ **Static variables** → class scope

### Type Casting
- ✅ Widening is automatic and safe
- ✅ Narrowing requires explicit cast
- ✅ Casting controls type compatibility

---

## 📚 Quick Reference

### Scanner Methods
```java
sc.next()          // Reads one token
sc.nextLine()      // Reads entire line
sc.nextInt()       // Reads integer
sc.nextDouble()    // Reads double
```

### Type Casting Hierarchy
```
byte → short → int → long → float → double
     ← (explicit cast required) ←
```

---

## 👨‍💻 Author

**Sumit**

- GitHub: [@LegendarySumit](https://github.com/LegendarySumit)

---

<div align="center">

**☕ Master the fundamentals, build anything**

*Java concepts with practical examples*

</div>