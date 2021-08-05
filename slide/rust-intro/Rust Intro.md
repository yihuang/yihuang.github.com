---
author: HuangYi(<huang@crypto.com>)
title: Rust Introduction
date: Aug 5, 2021
theme: solarized
---

# For C++ developers

## Basic data types

- Better type names
  - `u8`/`u16`/`u32`/`u64`/`i8`/`i16`/`i32`/`i64`/`usize`/`isize`
- [Explicit overflow behavior](https://doc.rust-lang.org/std/primitive.i64.html#method.checked_add)
  - Panic
  - Wrapping
  - Saturating
  - return `Option` or overflow flag

## Operator overloading

[doc](https://doc.rust-lang.org/rust-by-example/trait/ops.html)

```rust
impl ops::Add<Bar> for Foo {
    type Output = FooBar;

    fn add(self, _rhs: Bar) -> FooBar {
        FooBar
    }
}

fn main() {
    println!("Foo + Bar = {:?}", Foo + Bar);
}
```

## Struct

- Almost the same
-  `repr(C)` ensures the same layout as C
- unnamed field: `struct Rgb (i8, i8, i8)`
- tuple: `(i8, i8, i8)`
- empty struct: `struct Empty`

## Smart pointers

Used much less in rust than in c++ because of better reference and ownership system.

- `unique_ptr`: `Box`
- `shared_ptr`: `Rc`/`Arc`
  - [memory layout](https://doc.rust-lang.org/stable/src/alloc/sync.rs.html#311) is similar to `std::make_shared`

## RAII

- https://doc.rust-lang.org/rust-by-example/scope/raii.html

## Reference/pointer and memory safety

[Microsoft: 70 percent of all security bugs are memory safety issues](https://www.zdnet.com/article/microsoft-70-percent-of-all-security-bugs-are-memory-safety-issues/)

A typical c++ problematic program:

```c++
std::vector<int> arr = {1, ...};
int* a = &arr[0];
arr.push(2);
printf("%d\n", *a);
```

## Ownership system and move semantics

[doc](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)

- Each value in Rust has a variable that’s called its *owner*.
- There can only be one owner at a time.
- When the owner goes out of scope, the value will be dropped.

## Ownership system and move semantics

```c++
std::string s1("hello");
std::string s2(std::move(s1));
printf("%s, world!\n", s1.c_str());
// empty string
```

```rust
let s1 = String::from("hello");
let s2 = s1;
println!("{}, world!", s1);
// compile error
```

## Reference and Borrowing

[doc](https://doc.rust-lang.org/beta/rust-by-example/scope/borrow.html)

- Data can be immutably borrowed any number of times
- Only *one* mutable borrow is allowed at a time
- While immutably borrowed, mutable borrow is not allowed

```rust
let arr = vec![1, 2, ...];
let a = &arr[0];
arr.push(2);
println!("a: {}", a)
// compile error
```

## Fearless Concurrency

[Fearless Concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html#fearless-concurrency)

## Mutex API Design

```c++
std::mutex mtx;
void test() {
    std::lock_guard<std::mutex> lck (mtx);
    // do stuff
}
```

VS

```rust
fn test(locked_data: &Mutex<Data>) {
    let mut data = locked_data.lock().unwrap();
    // modify data
}
```

## Atomics

[doc](https://doc.rust-lang.org/std/sync/atomic/)

- The ordering semantics are the same as the c++ design.
- Only takes immutable reference to modify.

## Closure

```rust
let x = 4;
let equal_to_x = |z| z == x;
let y = 4;
assert!(equal_to_x(y));
```

- Similar to c++
- Different design in the type level, will cover this again in the section about trait.

# For Haskell developers

## Algebra data type

Play a game: How many inhabitants in a type?
- empty type
- unit type
- sum type
- product type

## Algebra data type

```rust
enum Type {
  Branch1(u8, u8),
  Branch2(bool, u16),
}
```

## Parameterized types (or Generics)

[doc](https://doc.rust-lang.org/beta/rust-by-example/generics.html)

```rust
fn foo<T: Display>(arg: T) -> () {
    println!("arg: {}", arg);
}
```

## trait

- [doc](https://doc.rust-lang.org/beta/rust-by-example/trait.html)

## Closure and trait

- Each closure have a unique type
- Classified by traits: `Fn/FnMut/FnOnce`
  - `FnOnce` consumes the captured variables
  - `FnMut` mutably borrow from the environment
  - `Fn` borrows immutably

## Phantom type

```rust
enum Inch {}
enum Mm {}

struct Length<Unit>(f64, PhantomData<Unit>);
```

Usages:

- [Mark the lifetime](https://doc.rust-lang.org/src/core/slice/iter.rs.html#71)
- [Encode business logic at type level](https://doc.rust-lang.org/rust-by-example/generics/phantom/testcase_units.html)

## Error handling

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

- Handle error explicitly

```rust
fn test() -> Result<u8, AppError> {
  if success {
    Ok(0)
  } else {
    Err(AppError::Reason1)
  }
}
```

## Error handling

- `?` Syntax sugar, error propagation.

```rust
fn test2() -> Result<(), AppError> {
  let a = test()?;
  println!("a: {}", a)
  Ok(())
}
```

# Zero Cost Abstraction

## Iterator

[Iterator faster than for loop](https://doc.rust-lang.org/book/ch13-04-performance.html)

```rust
certificate
  .extensions
  .iter()
  .find(|ext| ext.0 == &attestation_report_oid)
  .ok_or(EnclaveCertVerifierError::MissingAttestationReport)?;
```

## `NonZero*`

- `Option<NonZeroU32>`
  - has same size as `u32`

# Async

[async-book](https://rust-lang.github.io/async-book/01_getting_started/01_chapter.html)

# Real World Cases

- web backends
  - [rocket.rs](https://rocket.rs/)
- database plugins
  - [redis module](https://github.com/RedisLabsModules/redismodule-rs)
    - [example](https://github.com/cryptorelay/redis-aggregation)
  - [postgrseql extension](https://github.com/zombodb/pgx)
- front language for wasm

# Thanks