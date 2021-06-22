package com.change_vision.jude.api.test.model;

import com.change_vision.jude.api.inf.model.IAssociation;
import com.change_vision.jude.api.inf.model.IAttribute;
import com.change_vision.jude.api.inf.model.IClass;
import com.change_vision.jude.api.inf.model.IMultiplicityRange;
import junit.framework.Test;


public class IAttributeTest extends ITestCase {

    public static Test suite() {
        return suite("testModel/judeAPITest/IAttributeTest.jude", IAttributeTest.class);
    }

    public void testGetType_int() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute0");
        assertEquals("int", attr.getType().getName());
        assertEquals("int", attr.getTypeExpression());
    }

    public void testGetType_int_ARRAY() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute1");
        assertEquals("int", attr.getType().getName());
        assertEquals("int[]", attr.getTypeExpression());
    }

    public void testGetType_Class1() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute2");
        assertEquals("Class1", attr.getType().getName());
        assertEquals("Class1", attr.getTypeExpression());
    }

    public void testGetType_Class1_ARRAY() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute3");
        assertEquals("Class1", attr.getType().getName());
        assertEquals("Class1[][2]", attr.getTypeExpression());
    }

	public void testGetInitialValue_5() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute0");
        assertEquals("5", attr.getInitialValue());
	}

    public void testGetInitialValue_NONE() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute1");
        assertEquals("", attr.getInitialValue());
    }

	public void testIsChangeable_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute4");
        assertFalse(attr.isChangeable());
	}

    public void testIsChangeable_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute0");
        assertTrue(attr.isChangeable());
    }

    public void testIsChangeable_true_ASSOCIATION_END() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class4");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class5");
        assertFalse(attr.isChangeable());
    }

    public void testIsChangeable_false_ASSOCIATION_END() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class4");
        assertTrue(attr.isChangeable());
    }

    public void testIsDerived_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute5");
        assertTrue(attr.isDerived());
	}

    public void testIsDerived_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute0");
        assertFalse(attr.isDerived());
    }

    public void testIsDerived_true_ASSOCIATION_END() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class2");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class3");
        assertTrue(attr.isDerived());
    }

    public void testIsStatic_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute4");
        assertTrue(attr.isStatic());
    }

    public void testIsStatic_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute5");
        assertFalse(attr.isStatic());
    }

    public void testIsStatic_true_ASSOCIATION_END() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class4");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class5");
        assertTrue(attr.isStatic());
    }

    public void testIsStatic_false_ASSOCIATION_END() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class1");
        assertFalse(attr.isStatic());
    }

    public void testGetAssociation() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class1");
        assertNotNull(attr.getAssociation());
        assertTrue(attr.getAssociation() instanceof IAssociation);
    }

    public void testMultiplicity_None() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class1");
        assertEquals(IMultiplicityRange.UNDEFINED, attr.getMultiplicity()[0].getLower());
        assertEquals(IMultiplicityRange.UNDEFINED, attr.getMultiplicity()[0].getUpper());
    }

    public void testMultiplicity_ASTERISK() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class4");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class5");
        assertEquals(IMultiplicityRange.UNLIMITED, attr.getMultiplicity()[0].getLower());
        assertEquals(IMultiplicityRange.UNLIMITED, attr.getMultiplicity()[0].getUpper());
    }

    public void testMultiplicity_0_1() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class2");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class3");
        assertEquals(0, attr.getMultiplicity()[0].getLower());
        assertEquals(1, attr.getMultiplicity()[0].getUpper());
    }

    public void testMultiplicity_ATTRIBUTE() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute0");
        assertEquals(0, attr.getMultiplicity().length);
    }

	public void testIsComposite_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class4");
		assertTrue(attr.isComposite());
	}

    public void testIsComposite_false_1() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class4");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class5");
        assertFalse(attr.isComposite());
    }

    public void testIsComposite_false_2() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class0");
        assertFalse(attr.isComposite());
    }

	public void testIsAggregate_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class3");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class2");
        assertTrue(attr.isAggregate());
	}

    public void testIsAggregate_false_1() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class0");
        assertFalse(attr.isAggregate());
    }

    public void testIsAggregate_false_2() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class4");
        assertFalse(attr.isAggregate());
    }

    public void testIsEnable_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class4");
        assertTrue(attr.isEnable());
    }

    public void testIsEnable_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class0");
        assertFalse(attr.isEnable());
    }

    public void testQualifiers() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class1");
        IAttribute[] qualifiers = attr.getQualifiers();
        assertEquals(2, attr.getQualifiers().length);
        assertEquals("key0", qualifiers[0].getName());
        assertEquals("int", qualifiers[0].getType().getName());
        assertEquals("key1", qualifiers[1].getName());
    }

    public void testQualifiers_None() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class0");
        assertEquals(0, attr.getQualifiers().length);
    }
    
    public void testGetOwner() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute0");
        assertEquals(cls, attr.getOwner());
    }

    public void testGetOwner_ASSOCIATION_END() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class1");
        assertEquals(cls, attr.getOwner());
    }

    public void testIsPrivateVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute0");
        assertTrue(attr.isPrivateVisibility());
    }

    public void testIsPrivateVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute1");
        assertFalse(attr.isPrivateVisibility());
    }

    public void testIsPrivateVisibility_true_ASSOCIATION_END() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class1");
        assertTrue(attr.isPrivateVisibility());
    }

    public void testIsProtectedVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute1");
        assertTrue(attr.isProtectedVisibility());
    }

    public void testIsProtectedVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute2");
        assertFalse(attr.isProtectedVisibility());
    }

    public void testIsProtectedVisibility_true_ASSOCIATION_END() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class2");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class3");
        assertTrue(attr.isProtectedVisibility());
    }

    public void testIsPublicVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute2");
        assertTrue(attr.isPublicVisibility());
    }

    public void testIsPublicVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute3");
        assertFalse(attr.isPublicVisibility());
    }

    public void testIsPublicVisibility_true_ASSOCIATION_END() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class4");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class5");
        assertTrue(attr.isPublicVisibility());
    }

    public void testIsPackageVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute3");
        assertTrue(attr.isPackageVisibility());
    }

    public void testIsPackageVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute0");
        assertFalse(attr.isPackageVisibility());
    }

    public void testIsPackageVisibility_true_ASSOCIATION_END() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "class4");
        assertTrue(attr.isPackageVisibility());
    }
}
