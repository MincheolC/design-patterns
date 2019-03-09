## 장식자 (Decorator)

### 목적
객체에 동적으로 새로운 기능을 추가할 수 있게 한다.

### 동기
전체 클래스가 아닌 개별적인 객체에 새로운 기능을 추가할 필요가 있다. 이때 상속을 이용하게 되면 정적으로 처리가 되어 사용자가 원할때 제어할 수 없기 때문에 유용하지 못하다.

### 구조
- Component : 동적으로 추가할 서비스를 가질 가능성이 있는 객체들에 대한 인터페이스
- ConcreteComponent : 추가적인 서비스가 실제로 정의되어야 할 필요가 있는 객체
- Decorator : Component 객체에 대한 참조자를 관리하면서 Component에 정의된 인터페이스를 만족하도록 정의
- ConcreteDecorator : 새롭게 추가할 서비스를 실제로 구현하는 클래스

![composite](images/decorator.png)

### 활용
- 다른 객체에 영향을 주지 않고 각각의 객체에 새로운 기능을 추가하고 싶을때
- 제거될 수 있는 기능에 대해 사용
- 실제 상속으로 서브 클래스를 만드는 방법이 유용하지 못할때 사용

### 구현
- Decorator 객체의 인터페이스는 반드시 자신을 둘러싼 구성요소의 인터페이스를 만족
- Component 클래스는 가벼운 무게를 유지

[Decorator Example - window](https://github.com/betterdevstomorrow/design-patterns/tree/master/Structural_Patterns/decorator-example)

- Component
 ```cpp
class Widget {

public:
  virtual void draw() = 0;
  virtual ~Widget() {}
};
```

- ConcreteComponent

```cpp
class TextField : public Widget {

private:
   int width, height;

public:
   TextField( int w, int h ){
      width  = w;
      height = h;
   }

   void draw() {
      cout << "TextField: " << width << ", " << height << '\n';
   }
};
```

- Decorator
   
```cpp
class Decorator : public Widget {

private:
   Widget* wid;

public:
   Decorator( Widget* w )  {
     wid = w;
   }

   void draw() {
     wid->draw();
   }

   ~Decorator() {
     delete wid;
   }
};
```

- ConcreteDecorator

```java
/* ConcreteDecoratorA */
class BorderDecorator : public Decorator {

public:
   BorderDecorator( Widget* w ) : Decorator( w ) { }
   void draw() {
      Decorator::draw();
      cout << "   BorderDecorator" << '\n';
   }
};

/* ConcreteDecoratorB */
class ScrollDecorator : public Decorator {
public:
   ScrollDecorator( Widget* w ) : Decorator( w ) { }
   void draw() {
      Decorator::draw();
      cout << "   ScrollDecorator" << '\n';
   }
};
```

- Test

```java
int main( void ) {

   Widget* aWidget = new BorderDecorator(
                     new ScrollDecorator(
                     new TextField( 80, 24 )));
   aWidget->draw();
   delete aWidget;
}
```

### 이점
- 단순한 상속보다 설계의 융튱성을 더 많이 증대시킬 수 있다.
- 상위 클래스에 많은 기능이 몰려있는 상황을 피할 수 있다.

### 단점
- 작은 규모의 객체들이 많아져서 객체들을 모두 이해하고 있지 않는다면 유지보수가 어렵다.

### 적응자와 차이점
- 적응자는 인터페이스를 변경하지만 장식자는 객체를 변경한다.

### 참고
- [Decorator Pattern - wiki](
https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0_%ED%8C%A8%ED%84%B4)



---

- 스터디 날짜: 2019.3.10
- 스터디 참석자: 권현후, 김민경, 원지운, 전승훈, 전명훈, 차민철
