package equipment;

import java.util.Iterator;

public abstract class Equipment {
	private String name;

	public Equipment(String name) {
		this.name = name;
	}

	public abstract int power();

	public abstract int price();

	public abstract int discountPrice();

	public void add(Equipment eq) {
	};

	public void remove(Equipment eq) {
	}

	public Iterator<Equipment> createIterator() {
		return null;
	};
}
