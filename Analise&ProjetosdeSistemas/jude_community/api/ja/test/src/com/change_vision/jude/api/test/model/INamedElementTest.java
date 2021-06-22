package com.change_vision.jude.api.test.model;

import com.change_vision.jude.api.inf.model.IAttribute;
import com.change_vision.jude.api.inf.model.IClass;
import com.change_vision.jude.api.inf.model.IDependency;
import junit.framework.Test;

public class INamedElementTest extends ITestCase {

    public static Test suite() {
        return suite("testModel/judeAPITest/IElementTest.jude", INamedElementTest.class);
    }

    public void testGetName() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        // getOwnedElement() ÇÕ getName()ÇégópÇµÇƒÇ¢ÇÈÇΩÇﬂÅAclsÇ™nullÇ≈Ç»ÇØÇÍÇŒOK
		assertNotNull(cls);
	}

    public void testIsPublicVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        assertTrue(cls.isPublicVisibility());
    }

    public void testIsPublicVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        assertFalse(cls.isPublicVisibility());
    }

    public void testIsProtectedVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        assertTrue(cls.isProtectedVisibility());
    }

    public void testIsProtectedVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class2");
        assertFalse(cls.isProtectedVisibility());
    }

    public void testIsPackageVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class2");
        assertTrue(cls.isPackageVisibility());
    }

    public void testIsPackageVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class3");
        assertFalse(cls.isPackageVisibility());
    }

    public void testIsPrivateVisibility_true() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class3");
        assertTrue(cls.isPrivateVisibility());
    }

    public void testIsPrivateVisibility_false() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        assertFalse(cls.isPrivateVisibility());
    }

    public void testGetDefinition() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        assertEquals("The definition of Class0", cls.getDefinition());
    }

    public void testConstraints() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        IAttribute attr = (IAttribute)getElement(cls.getAttributes(), "attribute0");
        assertEquals(2, attr.getConstraints().length);
    }

    public void testGetSupplierDependencies() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        IDependency[] dependencies = cls.getSupplierDependencies();
        assertEquals(2, dependencies.length);
        assertEquals("dep2-1", dependencies[0].getName());
        assertEquals("dep3-1", dependencies[1].getName());
	}
    
//    public void testGetSupplierDependenciesWithObject() {
//        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
//        IDependency[] dependencies = cls.getSupplierDependencies();
//        assertEquals(1, dependencies.length);
//        assertEquals("dep8-5", dependencies[0].getName());
//    }
//    
//    public void testGetSupplierDependenciesWithClassifier() {
//        IClass cls = (IClass)getElement(project.getOwnedElements(), "Classifier0");
//        IDependency[] dependencies = cls.getSupplierDependencies();
//        assertEquals(1, dependencies.length);
//        assertEquals("self", dependencies[0].getName());
//    }
    
	public void testGetClientDependencies() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class1");
        IDependency[] dependencies = cls.getClientDependencies();
        assertEquals(2, dependencies.length);
        assertEquals("dep1-2", dependencies[0].getName());
        assertEquals("dep1-3", dependencies[1].getName());
	}
    
//    public void testGetClientDependenciesWithObject() {
//        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class5");
//        IDependency[] dependencies = cls.getClientDependencies();
//        assertEquals(1, dependencies.length);
//        assertEquals("dep5-6", dependencies[0].getName());
//   
//    }
    
//    public void testGetClientDependenciesWithClassifier() {
//        IClass cls = (IClass)getElement(project.getOwnedElements(), "Classifier0");
//        IDependency[] dependencies = cls.getClientDependencies();
//        assertEquals(1, dependencies.length);
//        assertEquals("self", dependencies[0].getName());
//    }
}
