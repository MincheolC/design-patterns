package function.impl;

public class IPhoneSimplePayImpl implements SimplePayImpl {
	@Override
	public void printLogo() {
		System.out.println("=== iPhone ===");
	}

	@Override
	public void authorize() {
		System.out.println("skip auth");
	}

	@Override
	public void pay(int price) {
		System.out.println("pay " + price + " won.");
	}

	@Override
	public void payNFC(int price) {
		System.out.println("dose not support NFC system.");
	}

	@Override
	public void enterAccount(String id) {
		System.out.println("regist account id: " + id);
	}

	@Override
	public void startApp(String appNm) {
		System.out.println("Start apple [" + appNm + "] Application");
	}
}
