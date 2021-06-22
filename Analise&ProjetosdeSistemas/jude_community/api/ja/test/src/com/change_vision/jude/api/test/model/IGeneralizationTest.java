package com.change_vision.jude.api.test.model;

import com.change_vision.jude.api.inf.model.IClass;
import com.change_vision.jude.api.inf.model.IGeneralization;
import junit.framework.Test;

public class IGeneralizationTest extends ITestCase {

    public static Test suite() {
        return suite("testModel/judeAPITest/IClassTest.jude", IGeneralizationTest.class);
    }

	public void testGetSubType() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
        IGeneralization[] generalizations = cls.getGeneralizations();  // 3-5, 4-5

        assertEquals(cls, generalizations[0].getSubType());
        assertEquals(cls, generalizations[1].getSubType());
	}

	public void testGetSuperType() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
        IGeneralization[] generalizations = cls.getGeneralizations();  // 3-5, 4-5

        IClass cls3 = (IClass)getElement(project.getOwnedElements(), "Class3");
        IClass cls4 = (IClass)getElement(project.getOwnedElements(), "Class4");

        assertEquals(cls3, generalizations[0].getSuperType());
        assertEquals(cls4, generalizations[1].getSuperType());
	}
}
