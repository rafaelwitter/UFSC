package com.change_vision.jude.api.test.model;

import com.change_vision.jude.api.inf.model.IAssociation;
import com.change_vision.jude.api.inf.model.IAssociationClass;
import com.change_vision.jude.api.inf.model.IAttribute;
import com.change_vision.jude.api.inf.model.IClass;
import junit.framework.Test;


public class IAssociationClassTest extends ITestCase {

    public static Test suite() {
        return suite("testModel/judeAPITest/IAssociationClassTest.jude", IAssociationClassTest.class);
    }

	public void testGetAttributes() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IAssociation association = cls.getAttributes()[0].getAssociation();
        assertTrue(association instanceof IAssociationClass);

        IClass aCls = (IClass)getElement(project.getOwnedElements(), "AssociationClass0");
        assertEquals(aCls, association);
        
        IAttribute[] attr = association.getAttributes();
        assertEquals(2, attr.length);
        assertEquals("class0", attr[0].getName());
        assertEquals("class1", attr[1].getName());
	}
}
