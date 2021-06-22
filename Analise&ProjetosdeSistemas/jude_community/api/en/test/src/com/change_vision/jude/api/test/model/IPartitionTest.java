package com.change_vision.jude.api.test.model;

import junit.framework.Test;

import com.change_vision.jude.api.inf.model.IActivity;
import com.change_vision.jude.api.inf.model.IActivityDiagram;
import com.change_vision.jude.api.inf.model.IDiagram;
import com.change_vision.jude.api.inf.model.IPartition;

public class IPartitionTest extends ITestCase {

    public static Test suite() {
        return suite("testModel/judeAPITest/IActivityDiagramTest.jude", IPartitionTest.class);
    }

    public void testAll() {
        IActivity activity = getActivity();
        
        IPartition[] partitions = activity.getPartitions();
        assertEquals(2, partitions.length);
        
        testDimension0(partitions[0]);
        testDimension1(partitions[1]);
    }
    
    private void testDimension0(IPartition partition) {
        assertEquals("dimension0", partition.getName());
        assertNull(partition.getSuperPartition());
        assertEquals(0, partition.getActivityNodes().length);
        
        IPartition[] subs = partition.getSubPartitions();
        assertEquals(2, subs.length);
        testP0(subs[0]);
        testP3(subs[1]);
    }

    private void testP0(IPartition partition) {
        assertEquals("P0", partition.getName());
        assertEquals("dimension0", partition.getSuperPartition().getName());
        assertEquals(0, partition.getActivityNodes().length);
        
        IPartition[] subs = partition.getSubPartitions();
        assertEquals(1, subs.length);
        assertEquals("P1", subs[0].getName());
        assertEquals(7, subs[0].getActivityNodes().length);
    }

    private void testP3(IPartition partition) {
        assertEquals("P3", partition.getName());
        assertEquals("dimension0", partition.getSuperPartition().getName());
        assertEquals(2, partition.getActivityNodes().length);
        
        IPartition[] subs = partition.getSubPartitions();
        assertEquals(0, subs.length);
    }

    private void testDimension1(IPartition partition) {
        assertEquals("dimension1", partition.getName());
        assertNull(partition.getSuperPartition());
        assertEquals(0, partition.getActivityNodes().length);
        
        IPartition[] subs = partition.getSubPartitions();
        assertEquals(1, subs.length);
        testP2(subs[0]);
    }

    private void testP2(IPartition partition) {
        assertEquals("P2", partition.getName());
        assertEquals("dimension1", partition.getSuperPartition().getName());
        assertEquals(9, partition.getActivityNodes().length);
        
        IPartition[] subs = partition.getSubPartitions();
        assertEquals(0, subs.length);
    }

    private IActivity getActivity() {
        IDiagram[] dgms = project.getDiagrams();
        for (int i = 0; i < dgms.length; i++) {
            IDiagram diagram = dgms[i];
            if ("ActivityDiagram0".equals(diagram.getName())) {
                return ((IActivityDiagram)diagram).getActivity();
            }
        }
        fail("no diagram");
        return null;
    }
}
