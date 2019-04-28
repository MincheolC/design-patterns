## 방문자(Visitor)

### 목적

구조와 동작 다른 인터페이스로 분리하여 서로 간 호출하도록 함으로써, 새로운 동작 추가를 자유롭게 하기 위해 사용된다.

### 구조

![Visitor](https://www.baeldung.com/wp-content/uploads/2018/06/Visitor-UML.png)

* Visitor: '동작'을 선언한 인터페이스. ConcreteElement마다 실행할 동작을 오버로딩해 선언해야 함.
* Element: '구조'를 선언한 인터페이스. 내부에서 Visitor를 호출하는 인터페이스를 선언해야 함.
* ObjectStructure: Element 인터페이스를 관리하기 위한 클래스. 복합체 패턴으로 관리할 수도 있고, 단순 리스트로 관리할 수도 있음.

### 활용

* 서로 구분되고 관계 없는 동작들을 하나의 객체 구조에서 수행하고, 클래스를 동작들로 '오염시키고' 싶지 않을 때.
* 객체 구조가 거의 변하지 않고, 하나의 기능만 새로 추가하고 싶을 때.

### 구현

> Interface

```java
interface Visitor {
  void visit(Wheel wheel);
  void visit(Engine engine);
  void visit(Body body);
  void visit(Car car);
}

interface Element {
  void accept(Visitor visitor);
}
```

> Concrete Class

```java
// Concrete Element
class Wheel implements Element {
  private String name;
  
  public Wheel(String name) {
    this.name = name;
  }
  
  public String getName() {
    return this.name;
  }
  
  public void accept(Visitor visitor) {
    visitor.visit(this);
  }
}

class Engine implements Element {
  public void accept(Visitor visitor) {
    visitor.visit(this);
  }
}

class Body implements Element {
  public void accept(Visitor visitor) {
    visitor.visit(this);
  }
}

class Car implements Element {
  Element[] elements;
  
  public Car() {
    this.elements = new Element[] { 
      new Wheel("front-left"),
      new Wheel("front-right"),
      new Wheel("back-right"),
      new Wheel("back-left"),
      new Body(),
      new Engine()
    };
  }
  
  public void accept(Visitor visitor) {
    for(Element elem : elements) {
      elem.accept(visitor);
    }
    visitor.visit(this);
  }
}
```

```java
// Concrete Visitor
class PrintVisitor implements Visitor {
  public void visit(Wheel wheel) {      
    System.out.println("Visiting " + wheel.getName() + " wheel");
  }

  public void visit(Engine engine) {
    System.out.println("Visiting engine");
  }

  public void visit(Body body) {
    System.out.println("Visiting body");
  }

  public void visit(Car car) {      
    System.out.println("Visiting car");
  }
}

class MoveVisitor implements Visitor {
  public void visit(Wheel wheel) {
    System.out.println("Kicking my " + wheel.getName() + " wheel");
  }

  public void visit(Engine engine) {
    System.out.println("Starting my engine");
  }

  public void visit(Body body) {
    System.out.println("Moving my body");
  }

  public void visit(Car car) {
    System.out.println("Starting my car");
  }
}
```

> Execute

```java
public class Main {
  static public void main(String[] args) {
    Element car = new Car();
    car.accept(new PrintVisitor());
    car.accept(new MoveVisitor());
  }
}
```

### 장점

* 객체 구조에 대한 동작구현을 객체 외부로 위임할 수 있다.
* 사용자 입장에서 매우 단순하게 전체 객체구조를 다룰 수 있게 한다.
* 구조과 동작을 분리했기 때문에, 안정적이고 확장에 용이한 구조로 만들 수 있다.

### 단점

* 객체가 추가될 때마다, Visitor에도 해당 객체를 추가해주어야 함.
* 객체간 결합도가 높은 편이고, Visitor가 객체의 속성값을 직접 제어하므로 캡슐화가 약해진다.

### 관련 패턴

* 복합체(Composite)
* 해석자(Interpreter)

### 참고

<http://blog.naver.com/PostView.nhn?blogId=2feelus&logNo=220664244510&parentCategoryNo=&categoryNo=28&viewDate=&isShowPopularPosts=false&from=postView>

<https://zetawiki.com/wiki/Visitor_%ED%8C%A8%ED%84%B4>
