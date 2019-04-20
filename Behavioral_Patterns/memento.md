# Memento

메멘토 패턴을 통해 객체의 상태를 저장해두고 이전 상태로 복구함

### 의도

객체의 내부 상태를 저장해두고 해당 객체가 그 상태로 되돌아 올 수 있도록 함.

### 다른 이름

토큰 (token)

### 문제

오류 복구, 연산 결과 수행 취소(undo) 등과 같은 때에 따라 객체의 내부 상태를 기록해 둘 필요가 있음.

### 활용성

- 객체의 상태에 대한 스냅샷을 저장한 후 나중에 이 상태로 복구해야 할 때
- 상태를 얻는 데 필요한 직접적인 인터페이스를 두면 객체의 세부 구현이 드러나기 때문에 캡슐화 하고 싶을 때

### 협력 방법

- Caretaker 객체는 Originator 객체에게 Memento 객체를 요구
- 받는 Memento 객체를 저장 함. (이전 상태로 돌아갈 필요가 없는 경우 Originator 객체가 Memento객체를 전달 안할 수도 있음.)
- Memento 객체는 Originator 객체만이 상태를 설정하고 읽어올 수 있음.

### 구조

- Caretaker 클래스는 memento에 대한 제한된 인터페이스만 볼 수 있음. 메멘토의 보관을 책임짐.
- Originator 클래스는 memento의 다양한 인터페이스를 볼 수 있음.
- 모든 상태를 저장하는 것이 아니라 변경된 정보들만 저장.

   ![mediator](images/memento.jpg)

### 결과

- 캡슐화 된 경계를 유지 가능.
    - 원조만 메멘토를 다룰 수 있기 떄문에 메멘토가 외부에 노출되지 않음.
- 원조 클래스를 단순화할 수 있음.

### 단점

- 메멘토의 사용으로 더 많은 비용이 들어갈 수 있음.
    - 원조 클래스가 많은 양의 정보를 저장하거나 상당히 자주 메멘토를 반환해야하면 오버헤드가 커질 수 있음. → 상태를 보호하고 복구하는 비용이 싸지 않으면 적합하지 않음
- 프로그래밍 언어에 따라 원조본 객체만 메멘토 상태에 접근할 수 있도록 보장하기가 힘들 수 있음.

### 관련 패턴

Command 패턴에서 실행 취소가 가능한 연산의 상태를 저장할 때, Iterator 패턴에서 반복 과정 상태를 관리할 때 Mementor를 사용 가능.

### 사용 예

- undo
- transaction
- checkpoint

[Memento Design Pattern - Memento Pattern in Java - HowToDoInJava](https://howtodoinjava.com/design-patterns/behavioral/memento-design-pattern/)
