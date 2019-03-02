package game.unit;

public class Main {

	public static void main(String[] args) {
		GameUnit.initUnitArray();

		GameUnit pUnit1 = AttackUnit.createInstance();
		if (pUnit1 == null) {
			System.out.println("No more create unit");
		}

		GameUnit pUnit2 = ProtectUnit.createInstance();
		if (pUnit2 == null) {
			System.out.println("No more create unit");
		}

		GameUnit.destroyUnit(pUnit1);
		GameUnit.destroyUnit(pUnit2);

	}

}
