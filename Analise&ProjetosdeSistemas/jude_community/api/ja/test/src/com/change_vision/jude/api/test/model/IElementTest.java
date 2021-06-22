package com.change_vision.jude.api.test.model;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;

import junit.framework.Test;

import com.change_vision.jude.api.inf.model.IComment;
import com.change_vision.jude.api.inf.model.IElement;
import com.change_vision.jude.api.inf.model.ITaggedValue;

public class IElementTest extends ITestCase {
    
    public static Test suite() {
        return suite("testModel/judeAPITest/IElementTest.jude", IElementTest.class);
    }

    public static Test suiteWithStream() {
        try {
            File file = new File("testModel/judeAPITest/IElementNonZipTest.jude");
            InputStream in = new FileInputStream(file);
            return suite(in, IElementTest.class);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static Test suiteWithZipStream() {
        try {
            InputStream in = new FileInputStream(
                   new File("testModel/judeAPITest/IElementTest.jude"));
           return suite(in, IElementTest.class);
       } catch (FileNotFoundException e) {
           e.printStackTrace();
           return null;
       }
    }

    public void testGetOwner() {
        IElement element = getElement(project.getOwnedElements(), "Class0");
        assertEquals(project, element.getOwner());
	}

    public void testGetOwner_null() {
        assertEquals(null, project.getOwner());
    }

	public void testGetStereotypes() {
        IElement element = getElement(project.getOwnedElements(), "Class0");
		String[] stereotypes = element.getStereotypes();
		assertEquals(2, stereotypes.length);
		assertEquals("stereotype", stereotypes[0]);
        assertEquals("stereotype2", stereotypes[1]);
	}

	public void testGetComments() {
        IElement element = getElement(project.getOwnedElements(), "Class0");
        IComment[] comments = element.getComments();
        assertEquals(2, comments.length);
	}

    public void testGetTaggedValues() {
        IElement element = getElement(project.getOwnedElements(), "UseCase0");
        ITaggedValue[] taggedValues = element.getTaggedValues();
        assertEquals(4, taggedValues.length);
    }
    
    public void testGetId() {
        IElement element = getElement(project.getOwnedElements(), "UseCase0");
        assertEquals("f19d6e-1077342f82b-f240dd135f0b4fbdf1febbfb27a0ca56", element.getId());
    }
}
