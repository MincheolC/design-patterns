package equipment.impl;

import java.util.Iterator;
import java.util.LinkedList;

import equipment.CompositeEquipment;
import equipment.Equipment;

public class Chassis extends CompositeEquipment {
	private LinkedList<Equipment> list;

	public Chassis(String name) {
		super(name);
		list = new LinkedList<>();
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
