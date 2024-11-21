
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    fn width(&self) -> bool {
        self.width > 0
    }
    fn height(&self) -> bool {
        self.height > 0
    }
}

enum List{
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

struct MyBox<T>(T);

impl<T> MyBox<T>{
    fn new(x:T) -> MyBox<T>{
        MyBox(x)
    }
}
use std::ops::Deref;

impl<T> Deref for MyBox<T>{
    type Target = T;
    fn deref(&self) -> &Self::Target{
        &self.0
    }
}

fn hello(name: &str) {
    println!("Hello, {name}!");
}

struct CustomSmartPointer{
    data:String,
}
impl Drop for CustomSmartPointer{
    fn drop(&mut self){
        println!("Dropping CustomSmartPointer with data `{}`!",self.data);
    }
}


fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
        
    );
    if rect1.width() {
        println!("The rectangle has a nonzero width; it is {}", rect1.width);
    }
    if rect1.height() {
        println!("The rectangle has a nonzero height; it is {}", rect1.height);
    }
    dbg!(&rect1);

    let list = Cons(1,Box::new(Cons(2,Box::new(Cons(3,Box::new(Nil))))));

    let m = MyBox::new(String::from("Test"));
    hello(&m);

    let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
    drop(c);
    let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
    println!("CustomSmartPointers created.");
    
    println!("Floating point comparison");

    let result = 0.1 + 0.2;
    let expected = 0.3;
    let difference = (result - expected);
    assert!(difference < std::f64::EPSILON);
    println!("The difference between the result and the expected value is: {}", difference);
}

