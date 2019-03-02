package function;

import function.impl.SimplePayImpl;
import function.impl.GalaxySimplePayImpl;
import function.impl.IPhoneSimplePayImpl;

public abstract class SimplePay {
	public static final String TYPE_IPHONE = "iPhone", TYPE_GALAXY = "galaxy";

	private SimplePayImpl impl;

	public SimplePayImpl getSimplePayImpl() {
		return impl;
	}

	public SimplePay setImpl(String type) {
		if (TYPE_IPHONE.equals(type)) {
			impl = new IPhoneSimplePayImpl();
		} else if (TYPE_GALAXY.equals(type)) {
			impl = new GalaxySimplePayImpl();
		}
		return this;
	}

	public void start() {
		impl.printLogo();
	}

	public abstract void execute();
}
