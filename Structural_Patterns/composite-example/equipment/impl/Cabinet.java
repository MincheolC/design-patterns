package equipment.impl;

import java.util.ArrayList;
import java.util.Iterator;

import equipment.CompositeEquipment;
import equipment.Equipment;

public class Cabinet extends CompositeEquipment {
	private ArrayList<Equipment> list;

	public Cabinet(String name) {
		super(name);
		list = new ArrayList<>();
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
