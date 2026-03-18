---
marp: true
theme: rmt-light-blue
headingDivider: [2, 3]
highlight: atom-one-dark
header: Code Highlighting Demo 2026
footer: Code Highlighting Demo 2026
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/a11y-light.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js"></script>

<script>hljs.highlightAll();</script>

## Code Highlighting Verification Document

This document verifies the `code highlighting` functionality of Refined Marp Theme and its display effects in different themes.

Add the following code to the beginning of your markdown file.

```html
<link
  rel="stylesheet"
  href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/a11y-light.min.css"
/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js"></script>

<script>
  hljs.highlightAll()
</script>
```

### Feature Highlights

- ✓ Pure CSS code coloring implementation
- ✓ Support for keyword, string, comment coloring
- ✓ Rounded border design
- ✓ Monospace font display
- ✓ Light/dark theme adaptation

### Java Code Example

```java
public class HelloWorld {
    public static void main(String[] args) {
        // Print Hello World
        System.out.println("Hello, World!");

        // Variable declaration
        int count = 10;
        String message = "Welcome to Java";

        // Loop example
        for (int i = 0; i < count; i++) {
            System.out.println("Count: " + i);
        }
    }
}
```

### Python Code Example

```python
# Python code highlighting example
def greet(name):
    """Greet the user"""
    return f"Hello, {name}!"

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]

# Class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I'm {self.name}, {self.age} years old.")
```

### JavaScript Code Example

```javascript
// JavaScript code highlighting example
const users = [
  { id: 1, name: 'Alice', age: 25 },
  { id: 2, name: 'Bob', age: 30 },
  { id: 3, name: 'Charlie', age: 35 },
]

// Arrow function
const filterUsers = (users, minAge) => {
  return users.filter(user => user.age >= minAge)
}

// Async function
async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`)
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error:', error)
  }
}
```

### TypeScript Code Example

```typescript
// TypeScript code highlighting example
interface User {
  id: number
  name: string
  email: string
  age?: number // Optional property
}

class UserService {
  private users: User[] = []

  addUser(user: User): void {
    this.users.push(user)
  }

  findUserById(id: number): User | undefined {
    return this.users.find(user => user.id === id)
  }

  // Generic method
  sortBy<T>(array: T[], key: keyof T): T[] {
    return array.sort((a, b) => (a[key] > b[key] ? 1 : -1))
  }
}
```

### Go Code Example

```go
package main

import "fmt"

// User struct
type User struct {
    Name string
    Age  int
}

// Method
func (u *User) Greet() string {
    return fmt.Sprintf("Hello, %s!", u.Name)
}

func main() {
    // Create user
    user := User{Name: "Alice", Age: 25}

    // Call method
    message := user.Greet()
    fmt.Println(message)

    // Slice operations
    numbers := []int{1, 2, 3, 4, 5}
    for _, num := range numbers {
        fmt.Printf("Number: %d\n", num)
    }
}
```

### Rust Code Example

```rust
// Rust code highlighting example
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn new(width: u32, height: u32) -> Self {
        Rectangle { width, height }
    }

    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect = Rectangle::new(10, 20);
    println!("Area: {}", rect.area());

    // Vectors and iterators
    let numbers: Vec<i32> = (1..=5).collect();
    let sum: i32 = numbers.iter().sum();
    println!("Sum: {}", sum);
}
```

### XML Code Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <appSettings>
        <add key="AppName" value="MyApp"/>
        <add key="Version" value="1.0.0"/>
        <add key="DebugMode" value="true"/>
    </appSettings>

    <connectionStrings>
        <add name="DefaultConnection"
             connectionString="Server=localhost;Database=mydb;"
             providerName="System.Data.SqlClient"/>
    </connectionStrings>
</configuration>
```

### YAML Code Example

```yaml
# Application configuration
app:
  name: 'My Application'
  version: 1.0.0
  debug: true

# Server configuration
server:
  host: localhost
  port: 8080
  ssl:
    enabled: true
    certificate: /path/to/cert.pem

# Database configuration
database:
  driver: postgresql
  host: db.example.com
  port: 5432
  name: myapp_db
  credentials:
    username: admin
    password: secret123

# Logging configuration
logging:
  level: info
  format: json
  output:
    - stdout
    - /var/log/myapp.log
```

### Dark Theme Verification

<!-- _theme: rmt-dark-blue -->

#### Dark Theme Java Code

```java
public class DarkThemeDemo {
    public static void main(String[] args) {
        System.out.println("Dark theme code highlighting!");
    }
}
```

#### Dark Theme Python Code

```python
# Dark theme Python example
def dark_theme_demo():
    print("Dark theme Python code!")
    return True
```

#### Dark Theme JavaScript Code

```javascript
// Dark theme JavaScript example
const demo = () => {
  console.log('Dark theme JavaScript!')
}
```
