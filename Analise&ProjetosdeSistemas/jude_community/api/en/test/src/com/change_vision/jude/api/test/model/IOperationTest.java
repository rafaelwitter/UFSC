package com.change_vision.jude.api.test.model;

import com.change_vision.jude.api.inf.model.IClass;
import com.change_vision.jude.api.inf.model.IOperation;
import junit.framework.Test;

public class IOperationTest extends ITestCase {

    public static Test suite() {
        return suite("testModel/judeAPITest/IOperationTest.jude", IOperationTest.class);
    }

	public void testParameters_0() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation1");
        assertEquals(0, op.getParameters().length);
	}

    public void testParameters_2() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation3");
        assertEquals(2, op.getParameters().length);
        assertEquals("param0", op.getParameters()[0].getName());
        assertEquals("param1", op.getParameters()[1].getName());
    }

	public void testReturnType_void() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation1");
        assertEquals("void", op.getReturnType().getName());
        assertEquals("void", op.getReturnTypeExpression());
	}

    public void testReturnType_Class1() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation2");
        assertEquals("Class1", op.getReturnType().getName());
        assertEquals("Class1", op.getReturnTypeExpression());
    }

    public void testReturnType_Class1_ARRAY3() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation3");
        assertEquals("Class1", op.getReturnType().getName());
        assertEquals("Class1[3]", op.getReturnTypeExpression());
    }

    public void testReturnType_null() { // for constructor
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation4");
        assertEquals(null, op.getReturnType());
        assertEquals("", op.getReturnTypeExpression());
    }

    public void testIsAbstract_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation1");
        assertTrue(op.isAbstract());
	}

    public void testIsAbstract_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation0");
        assertFalse(op.isAbstract());
    }

	public void testIsStatic_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation0");
        assertTrue(op.isStatic());
	}

    public void testIsStatic_final() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation1");
        assertFalse(op.isStatic());
    }

    public void testIsLeaf_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation0");
        assertTrue(op.isLeaf());
    }

    public void testIsLeaf_final() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation1");
        assertFalse(op.isLeaf());
    }

    public void testIsPublicVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation0");
        assertTrue(op.isPublicVisibility());
    }

    public void testIsPublicVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation1");
        assertFalse(op.isPublicVisibility());
    }

    public void testIsProtectedVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation1");
        assertTrue(op.isProtectedVisibility());
    }

    public void testIsProtectedVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation2");
        assertFalse(op.isProtectedVisibility());
    }

    public void testIsPackageVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation2");
        assertTrue(op.isPackageVisibility());
    }

    public void testIsPackageVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation3");
        assertFalse(op.isPackageVisibility());
    }

    public void testIsPrivateVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation3");
        assertTrue(op.isPrivateVisibility());
    }

    public void testIsPrivateVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation0");
        assertFalse(op.isPrivateVisibility());
    }
}
