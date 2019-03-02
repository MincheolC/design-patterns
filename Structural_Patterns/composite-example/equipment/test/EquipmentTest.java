package equipment.test;

import org.junit.Test;

import equipment.impl.Bus;
import equipment.impl.Cabinet;
import equipment.impl.Card;
import equipment.impl.Chassis;
import equipment.impl.FloppyDisk;

public class EquipmentTest {

	@Test
	public void test() {
		Cabinet cabinet = new Cabinet("PC Cabinet");
		Chassis chassis = new Chassis("PC Chassis");

		cabinet.add(chassis);

		Bus bus = new Bus("MCA Bus");
		bus.add(new Card("16Mbs Token Ring"));
		chassis.add(bus);
		chassis.add(new FloppyDisk("3.5bin Floppy"));

		System.out.println("The new price is " + chassis.price() + " won.");
	}

}
