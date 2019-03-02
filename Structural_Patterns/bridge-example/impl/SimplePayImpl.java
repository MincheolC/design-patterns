package function.impl;

public interface SimplePayImpl {

	public void printLogo();

	public void startApp(String appNm);

	public void authorize();

	public void pay(int price);

	public void payNFC(int price);

	public void enterAccount(String id);

}
