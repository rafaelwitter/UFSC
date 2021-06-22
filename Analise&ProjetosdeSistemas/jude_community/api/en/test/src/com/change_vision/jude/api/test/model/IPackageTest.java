package com.change_vision.jude.api.test.model;

import com.change_vision.jude.api.inf.model.INamedElement;
import com.change_vision.jude.api.inf.model.IPackage;
import junit.framework.Test;

public class IPackageTest extends ITestCase {

    public static Test suite() {
        return suite("testModel/judeAPITest/IPackageTest.jude", IPackageTest.class);
    }

	public void testOwnedElements() {
        INamedElement[] ownedElements = getOwnerElements();
        
        assertNotNull(getElement(ownedElements, "package0"));
        assertNotNull(getElement(ownedElements, "Subsystem0"));
        assertNotNull(getElement(ownedElements, "Actor0"));
        assertNotNull(getElement(ownedElements, "UseCase0"));
        assertNotNull(getElement(ownedElements, "Interface0"));
        assertNotNull(getElement(ownedElements, "Class0"));
        assertNotNull(getElement(ownedElements, "Entity0"));
        assertNotNull(getElement(ownedElements, "AssociationClass0"));
		
        assertNull(getElement(ownedElements, "Class Diagram0"));
        assertNull(getElement(ownedElements, "UseCase Diagram0"));
        assertNull(getElement(ownedElements, "Sequence Diagram0"));
        assertNull(getElement(ownedElements, "Component Diagram0"));
        assertNull(getElement(ownedElements, "Deployment Diagram0"));

        assertNull(getElement(ownedElements, "association0"));
        assertNull(getElement(ownedElements, "dependency0"));
        assertNull(getElement(ownedElements, "generalization0"));
        assertNull(getElement(ownedElements, "realization0"));
        assertNull(getElement(ownedElements, "include0"));
        assertNull(getElement(ownedElements, "extend0"));
        assertNull(getElement(ownedElements, "link0"));
        assertNull(getElement(ownedElements, "Object0"));
        assertNull(getElement(ownedElements, "Component0"));
        assertNull(getElement(ownedElements, "Artifact0"));
        assertNull(getElement(ownedElements, "Node0"));
        assertNull(getElement(ownedElements, "ComponentInstance0"));
        assertNull(getElement(ownedElements, "NodeInstance0"));
	}
	
	public void testERModel() {
		IPackage testPkg = (IPackage)getElement(project.getOwnedElements(), "er_model");
		assertNull(testPkg);
	}

    protected INamedElement[] getOwnerElements() {
        IPackage testPkg = (IPackage)getElement(project.getOwnedElements(), "package");
		return testPkg.getOwnedElements();
    }
}
