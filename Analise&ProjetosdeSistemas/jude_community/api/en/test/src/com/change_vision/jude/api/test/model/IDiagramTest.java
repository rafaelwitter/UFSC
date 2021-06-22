package com.change_vision.jude.api.test.model;

import junit.framework.Test;

import com.change_vision.jude.api.inf.model.IDiagram;

public class IDiagramTest extends ITestCase {

    public static Test suite() {
        return suite("testModel/judeAPITest/IActivityDiagramTest.jude", IDiagramTest.class);
    }

    public void testGetTexts() {
        IDiagram[] dgms = project.getDiagrams();
        for (int i = 0; i < dgms.length; i++) {
            IDiagram diagram = dgms[i];
            if ("アクティビティ図0".equals(diagram.getName())) {
                String[] texts = diagram.getText();
                assertEquals("テキスト1", texts[0]);
                assertEquals("テキスト2", texts[1]);
                assertEquals("テキスト3", texts[2]);
            }
        }
    }
}
