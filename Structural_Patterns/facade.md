## 퍼사드 (Facade)

### 목적
서브시스템을 사용하기 쉽도록 상위 수준의 인터페이스를 정의

### 동기
서브시스템들 사이의 의사소통 및 종속성을 최소화하기 위해 주어진 서브시스템의 일반적인 기능에 대한 단순화된 하나의 인터페이스를 제공

### 구조

![composite](images/facade.jpg)

### 활용
- 복잡한 서브시스템에 대한 단순한 인터페이스 제공이 필요할 때
- 추상 개념에 대한 구현 클래스와 사용자 사이에 너무 많은 종속성이 존재할 때
- 서브시스템을 계층화시킬 때

### 구현
- 사용자와 서브시스템 간의 결합도 줄이기
- 서브시스템 클래스 중 공개할 것과 감출 것 정하기

[Facade Example - computer](https://github.com/betterdevstomorrow/design-patterns/tree/master/Structural_Patterns/facade-example)

- CPU 클래스
 ```java
class CPU {
    public void freeze() { ... }
    public void jump(long position) { ... }
    public void execute() { ... }
}
```

- Memory 클래스
 ```java
class Memory {
    public void load(long position, byte[] data) { ... }
}
```

- HardDrive 클래스
 ```java
class HardDrive {
    public byte[] read(long lba, int size) { ... }
}
```

- Facade
 ```java
class Computer {
    private CPU cpu;
    private Memory memory;
    private HardDrive hardDrive;
  
    public Computer() {
        this.cpu = new CPU();
        this.memory = new Memory();
        this.hardDrive = new HardDrive();
    }
  
    public void startComputer() {
        cpu.freeze();
        memory.load(BOOT_ADDRESS, hardDrive.read(BOOT_SECTOR, SECTOR_SIZE));
        cpu.jump(BOOT_ADDRESS);
        cpu.execute();
    }
}
```

- Client
 ```java
class You {
    public static void main(String[] args) {
        Computer facade = new Computer();
        facade.startComputer();
    }
}
```

### 이점
- 서브시스템의 구성요소를 보호할 수 있다.
- 서브시스템과 사용자 코드 간의 결합도를 더욱 약하게 만든다.
- 퍼사드를 사용하거나 직접 서브시스템의 클래스를 사용할 수도 있다.

### 단점
- 퍼사드는 새로운 기능을 추가하거나 새로운 추가 기능에 대해 알 수 없다.

### 적응자와 차이점
- 적응자는 적응 대상 클래스에서 특성을 상속받아 적응 대상자에 정의된 인터페이스를 마치 자신이 제공하는것처럼 보여주는 패턴이며 퍼사드는 하나의 객체로 전체 서브 시스템을 표현하는 패턴이다.

### 참고
- [Facade Pattern - wiki](
https://ko.wikipedia.org/wiki/%ED%8D%BC%EC%82%AC%EB%93%9C_%ED%8C%A8%ED%84%B4)



---

- 스터디 날짜: 2019.3.10
- 스터디 참석자: 권현후, 김민경, 원지운, 전승훈, 전명훈, 차민철
