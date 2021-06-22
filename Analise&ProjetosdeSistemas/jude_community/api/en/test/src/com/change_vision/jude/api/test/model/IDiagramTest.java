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
            if ("�A�N�e�B�r�e�B�}0".equals(diagram.getName())) {
                String[] texts = diagram.getText();
                assertEquals("�e�L�X�g1", texts[0]);
                assertEquals("�e�L�X�g2", texts[1]);
                assertEquals("�e�L�X�g3", texts[2]);
            }
        }
    }
}
