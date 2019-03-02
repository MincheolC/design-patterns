package equipment;

import java.util.Iterator;

public class CompositeEquipment extends Equipment {
	

	public CompositeEquipment(String name) {
		super(name);
	}

	@Override
	public int power() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int price() {
		Iterator<Equipment> list = createIterator();
		int total = 0;
		while (list.hasNext()) {
			total += list.next().price();
		}
		list = null;
		return total;
	}

	@Override
	public int discountPrice() {
		// TODO Auto-generated method stub
		return 0;
	}


}
