package com.change_vision.jude.api.test.model;

import com.change_vision.jude.api.inf.model.IClass;
import junit.framework.Test;

public class IClassTest extends ITestCase {

    public static Test suite() {
        return suite("testModel/judeAPITest/IClassTest.jude", IClassTest.class);
    }

    public void testIsAbstract_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        assertTrue(cls.isAbstract());
    }

    public void testIsAbstract_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        assertFalse(cls.isAbstract());
    }

    public void testIsLeaf_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        assertTrue(cls.isLeaf());
    }

    public void testIsLeaf_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        assertFalse(cls.isLeaf());
    }

    public void testIsActive_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        assertTrue(cls.isActive());
    }

    public void testIsActive_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        assertFalse(cls.isActive());
    }

    public void testGetAttributes() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        assertEquals(2, cls.getAttributes().length);
	}

	public void testGetOperations() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        assertEquals(2, cls.getOperations().length);
	}

	public void testGetNestedClasses() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        assertEquals(2, cls.getNestedClasses().length);
	}

	public void testGetGeneralizations() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
        assertEquals(2, cls.getGeneralizations().length);
        assertEquals("3-5", cls.getGeneralizations()[0].getName());
        assertEquals("4-5", cls.getGeneralizations()[1].getName());
	}

	public void testGetSpecializations() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
        assertEquals(2, cls.getSpecializations().length);
        assertEquals("5-6", cls.getSpecializations()[0].getName());
        assertEquals("5-7", cls.getSpecializations()[1].getName());
	}

	public void testSupplierRealizations() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Interface1");
        assertEquals(2, cls.getSupplierRealizations().length);
        assertEquals("I1-C8", cls.getSupplierRealizations()[0].getName());
        assertEquals("I1-C9", cls.getSupplierRealizations()[1].getName());
	}

	public void testClientRealizations() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class8");
        assertEquals(2, cls.getClientRealizations().length);
        assertEquals("I0-C8", cls.getClientRealizations()[0].getName());
        assertEquals("I1-C8", cls.getClientRealizations()[1].getName());
	}
}
