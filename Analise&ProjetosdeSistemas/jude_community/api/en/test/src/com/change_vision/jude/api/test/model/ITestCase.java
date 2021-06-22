/*
 * Created on 2005/11/09
 */
package com.change_vision.jude.api.test.model;

import java.io.IOException;
import java.io.InputStream;

import junit.extensions.TestSetup;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import com.change_vision.jude.api.inf.model.IModel;
import com.change_vision.jude.api.inf.model.INamedElement;
import com.change_vision.jude.api.inf.project.ProjectAccessor;
import com.change_vision.jude.api.inf.project.ProjectAccessorFactory;

public abstract class ITestCase extends TestCase {

    private static ProjectAccessor prjAccessor;
    protected static IModel project;
    
    protected static Test suite(final String filePath, Class cls) {
        TestSuite testSuite = new TestSuite(cls);
        TestSetup wrapper = new TestSetup(testSuite) {
            protected void setUp() {
                try {
                    prjAccessor = ProjectAccessorFactory.getProjectAccessor();
                    prjAccessor.open(filePath);
                    project = prjAccessor.getProject();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            protected void tearDown() {
                prjAccessor.close();
            }
        };
        return wrapper;
    }

    protected static Test suite(final InputStream in, Class cls) {
        TestSuite testSuite = new TestSuite(cls);
        TestSetup wrapper = new TestSetup(testSuite) {
            protected void setUp() {
                try {
                    prjAccessor = ProjectAccessorFactory.getProjectAccessor();
                    prjAccessor.open(in);
                    project = prjAccessor.getProject();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            protected void tearDown() {
                prjAccessor.close();
                try {
                    in.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        };
        return wrapper;
    }

    protected INamedElement getElement(INamedElement[] elements, String elementName) {
        for (int i = 0; i < elements.length; i++) {
            if (elements[i].getName().equals(elementName)) {
                return elements[i];
            }
        }
        return null;
    }
}
