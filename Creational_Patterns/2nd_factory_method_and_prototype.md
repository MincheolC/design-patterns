## 팩토리 메서드 (Factory Method)

### 목적
객체를 생성하기 위한 인터페이스를 정의하지만, 어떤 클래스의 인스턴스를 생성할지에 대한 결정은 서브클래스에 위임한다

### 활용
- 어떤 클래스가 자신이 생성해야 하는 객체의 클래스를 예측할 수 없을 때
- 생성할 객체를 기술하는 책임을 자신의 서브클래스가 지정했으면 할 때
- 객체 생성의 책임을 몇 개의 보조 서브클래스 가운데 하나에게 위임하고, 어떤 서브클래스가 위임자인지에 대한 정보를 국소화시키고 싶을 때

### 이점
- 클라이언트 코드와 객체를 생성 하는 방법과 분리한다
- 시스템이 어떤 구체 클래스를 사용하는지에 대한 정보를 캡슐화한다
- 클라이언트 코드는 인터페이스와만 동작하기 때문에, 사용자가 정의한 어떤 서브클래스와도 동작할 수 있다

### 구현
1. 추상 클래스 정의: 추상 클래스(또는 인터페이스)로 정의하고, 서브클래스에서 정의한 팩토리 메서드를 대한 구현한다
2. 매개변수화: 팩토리 메서드가 매개변수를 받아서 어떤 종류의 제품을 생성할지 식별하게 만든다
    - JDK 사용 사례
       - java.util.Calendar#createCalendar()
       - java.text.NumberFormat#getInstance()

### 예제코드
##### 1. 추상 클래스 정의 예제
- [추상 클래스 코드](https://github.com/betterdevstomorrow/DesignPatterens/blob/master/src/main/java/chapter03/factorymethod/MazeGame.java)
```
public abstract class MazeGame {
    public Maze createMaze() {
        // ...
    }
    // 팩토리 메서드들
    public abstract Room makeRoom(int n);
    public abstract Wall makeWall();
    public abstract Door makeDoor(Room r1, Room r2);
```

- [서브클래스 코드](https://github.com/betterdevstomorrow/DesignPatterens/blob/master/src/main/java/chapter03/factorymethod/EnchantedMazeGame.java)
```
public class EnchantedMazeGame extends MazeGame {
    // 팩토리 메서드들
    @Override
    public Room makeRoom(int n) {
        return new EnchantedRoom(n);
    }
    @Override
    public Wall makeWall() {
        return new Wall();
    }
    @Override
    public Door makeDoor(Room r1, Room r2) {
        return new DoorNeedingSpell(r1, r2);
    }
}
```

- [호출 테스트 코드](https://github.com/betterdevstomorrow/DesignPatterens/blob/master/src/test/java/chapter03/factorymethod/MazeGameTest.java)
```
@Test
public void createEnchantedMaze() throws Exception {
    MazeGame mazeGame = new EnchantedMazeGame();
    Maze maze = mazeGame.createMaze();
}
```

##### 2. 매개변수화 예제 [(Ref. https://www.tutorialspoint.com/design_pattern/factory_pattern.htm)]
- 매개변수화된 팩토리 메서드 코드
```
public class ShapeFactory {
   public Shape getShape(String shapeType){
      if(shapeType.equalsIgnoreCase("CIRCLE"))   return new Circle();
      else if(shapeType.equalsIgnoreCase("RECTANGLE"))  return new Rectangle();
      else if(shapeType.equalsIgnoreCase("SQUARE"))  return new Square();
      return null;
   }
}
```

- 호출 코드
```
public static void main(String[] args) {
      ShapeFactory shapeFactory = new ShapeFactory();
      Shape shape1 = shapeFactory.getShape("CIRCLE");
      Shape shape2 = shapeFactory.getShape("RECTANGLE");
      Shape shape3 = shapeFactory.getShape("SQUARE");
   }
```

### 단점
- 제품 클래스가 바뀔 때마다 새로운 서브클래스를 생성해야 한다
- 서브 클래스가 너무 많이 만들어진다

### 참고
 - [Design Patterns Tutorial - Factory Pattern](https://www.tutorialspoint.com/design_pattern/factory_pattern.htm)


## 원형 (Prototype)

### 목적
원형이 되는(prototypical) 인스턴스를 사용하여 생성할 객체의 종류를 명시하고, 이렇게 만든 견본을 복사해서 새로운 객체를 생성

### 활용
- 제품의 생성, 복합, 표현 방법에 독립적인 제품을 만들고자 할 때
- 제품 클래스 계통과 병렬적으로 만드는 팩토리 클래스를 피하고 싶을 때
- 클래스의 인스턴스들이 서로 다른 상태 조합 중에 어느 하나일 때

### 이점
- object 생성에 높은 비용이 사용되는 경우 (DB에서 데이터를 가져오는 등) 원형 객체를 복사하여 비용을 줄일 수 있다
- 다른 생성패턴에 비해 클래스 수를 줄일 수 있다

### 단점
- 모든 제품에 clone 메서드 구현
- clone 메서드 구현시 주의사항
    - 언어에서 제공하는 복제 기능 사용 시 얕은 복사(shallow copy) 대 깊은 복사(deep copy) 문제 발생 가능
    - (일부 언어) 언어에서 제공하는 복제 기능 대신 복사 생성자 혹은 복사 팩토리 사용 권장
    
[복사 생성자/복사 팩토리 (자바 코드)]
```
public class Door extends MapSite {
    private Room room1;
    private Room room2;
    
    public Door(Room room1, Room room2) {
        this.room1 = room1;
        this.room2 = room2;
    }

    // 복사 생성자
    public Door(Door other) {
        this.room1 = other.room1;
        this.room2 = other.room2;
    }

    // 복사 팩토리
    public static Door newInstance(Door other) {
        return new Door(other.room1, other.room2);
    }
}
```

### 참고
 - [Python Design Patterns Tutorial - Prototype](https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_prototype.htm)
 - [Java Prototype Pattern](https://blog.seotory.com/post/2015/09/java-prototype-pattern)


---

- 스터디 날짜: 2019.2.17
- 스터디 참석자: 권현후, 김민경, 원지운, 전승훈, 전명훈, 차민철
