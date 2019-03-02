package function.impl;

public class GalaxySimplePayImpl implements SimplePayImpl {

	@Override
	public void printLogo() {
		System.out.println("=== Samsung ===");
	}

	@Override
	public void authorize() {
		System.out.println("Authorize by fingerprint");
	}

	@Override
	public void pay(int price) {
		galaxyPay(price);
	}

	@Override
	public void payNFC(int price) {
		galaxyPay(price);
	}

	private void galaxyPay(int price) {
		System.out.println("pay " + price + " won.");
	}

	@Override
	public void enterAccount(String id) {
		System.out.println("regist account id: " + id);
	}

	@Override
	public void startApp(String appNm) {
		System.out.println("Start android [" + appNm + "] Application");
	}

}
