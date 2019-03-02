package equipment.impl;

import java.util.Iterator;
import java.util.TreeSet;

import equipment.CompositeEquipment;
import equipment.Equipment;

public class Bus extends CompositeEquipment {
	private TreeSet<Equipment> list;

	public Bus(String name) {
		super(name);
		list = new TreeSet<Equipment>((a, b) -> a.price() - b.price());
	}

	@Override
	public void add(Equipment eq) {
		list.add(eq);
	};

	@Override
	public void remove(Equipment eq) {
		list.remove(eq);
	}

	@Override
	public Iterator<Equipment> createIterator() {
		return list.iterator();
	};

}
