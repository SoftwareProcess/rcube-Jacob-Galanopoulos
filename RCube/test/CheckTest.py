'''
Created on Oct 22, 2020

@author: jakeg
'''
import unittest
import RCube.check as check


class Test(unittest.TestCase):


    def test100_010_NominalFullCheck(self):
        expectedResult = {'status': 'full'}
        parms = {'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo',
                 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test100_020_NominalSpotsCheck(self):
        expectedResult = {'status': 'spots'}
        parms = {'cube': 'rrrrbrrrryyyyryyyyoooogoooowwwwowwwwbbbbybbbbggggwgggg',
                 'integrity': '8BE0EEDF13B2B464A2C7A120E6104AC7039B758E93D6F65651616FBBEED9A1EF'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_030_NominalCrossesCheck(self):
        expectedResult = {'status': 'crosses'}
        parms = {'cube': 'ybybbbybybrbrrrbrbwgwgggwgwgygyyygygrorooororowowwwowo',
                 'integrity': 'CE16F6174A8E0339E556FFDD1358AA56A03B1EB548AC31E324E52AAD7DC8BEF9'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_040_NominalUnknownCheck(self):
        expectedResult = {'status': 'unknown'}
        parms = {'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy',
                 'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test200_910_MissingCubeValue(self):
        expectedResult = {'status': 'error: missing cube value'}
        parms = {'cube': ''}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_915_MissingCubeKey(self):
        expectedResult = {'status': 'error: missing cube key'}
        parms = {'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_920_Not6CubeFaces(self):
        expectedResult = {'status': 'error: cube does not have correct number of elements'}
        parms = {'cube': '11111111122222222233333333344444444455555555566666666',
                 'integrity': '825E9253B6D7DB91050DA156E2CF524AE9B532B0C9C3DF89B01F18592850D5D3'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_925_Not6UniqueCubeFaces(self):
        expectedResult = {'status': 'error: cube does not have 6 distinct faces'}
        parms = {'cube': '111111111222222222333333333444444444555555555111111111',
                 'integrity': '93C6A03A7B2F9F5D319128523FA96AB3C748C67EAA6FDD4DAC8311F4D0393921'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_930_Not9CubeStickersPerSide(self):
        expectedResult = {'status': 'error: cube does not exactly have 9 of each element'}
        parms = {'cube': '111111111222222222333333333444444444555555555666666665',
                 'integrity': 'FFFA07BE4BF1438C0C660DE9E9C0624640DC23856E875F6730F6195CEAF2AB61'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test200_940_CubeDoesNotHaveDistinctCenterElements(self):
        expectedResult = {'status': 'error: cube does not exactly have distinct center elements'}
        parms = {'cube': '111141111222222222333333333144444444555555555666666666',
                 'integrity': 'A76983334BA3061D574662C5329E509475845E980971BC0ED0B5288FE2757C31'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test200_950_CubeHasImpossibleCorner(self):
        expectedResult = {'status': 'error: cube has a corner that can not exist'}
        parms = {'cube': '112111111522222222333333333444444444555555551666666666',
                 'integrity': '5572DDB8ED3FF835CFA36C776D8EC29CFD55F134046CFE0169AABD3AD4C4DE9B'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_955_CubeHasImpossibleEdge(self):
        expectedResult = {'status': 'error: cube has an edge that can not exist'}
        parms = {'cube': '111112111222122222333333333444444444555555555666666666',
                 'integrity': '61E17B21DC3147541FD168E65EDFACD2E5B302646450329B5848D6343D55129D'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_960_CubeHasWrongIntegrityValue(self):
        expectedResult = {'status': 'error: incorrect integrity value'}
        parms = {'cube': '111111111222222222333333333444444444555555555666666666',
                 'integrity': '88d897bd22e132d21a538745e63995b07d7c52ce9617a0979520545753ee0ded'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_960_CubeHasMissingIntegrityValue(self):
        expectedResult = {'status': 'error: missing integrity value'}
        parms = {'cube': '11111111122222222233333333344444444455555555566666666',
                 'integrity': ''}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_960_CubeHasMissingIntegrityKey(self):
        expectedResult = {'status': 'error: missing integrity key'}
        parms = {'cube': '11111111122222222233333333344444444455555555566666666'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_010_NominalEdgeValidEdges(self):
        expectedResult = {'result': 'true'}
        parms = {'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy',
                 'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        actualResult = check._validateEdges(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test110_020_NominalEdgeInvalidEdges(self):
        expectedResult = {'result': 'false'}
        parms = {'cube': '111112111222122222333333333444444444555555555666666666',
                 'integrity': '61E17B21DC3147541FD168E65EDFACD2E5B302646450329B5848D6343D55129D'}
        actualResult = check._validateEdges(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test210_910_EdgeMissingCubeValue(self):
        expectedResult = {'result': 'error: missing cube value'}
        parms = {'cube': ''}
        actualResult = check._validateEdges(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test210_920_EdgeMissingCubeKey(self):
        expectedResult = {'error': 'error: missing cube key'}
        parms = {}
        actualResult = check._validateEdges(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test120_010_NominalCornerValidCorners(self):
        expectedResult = {'result': 'true'}
        parms = {'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy',
                 'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        actualResult = check._validateEdges(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test120_020_NominalCornerInvalidCorners(self):
        expectedResult = {'result': 'false'}
        parms = {'cube': '112111111522222222333333333444444444555555551666666666',
                 'integrity': '5572DDB8ED3FF835CFA36C776D8EC29CFD55F134046CFE0169AABD3AD4C4DE9B'}
        actualResult = check._validateEdges(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test220_910_CornerMissingCubeValue(self):
        expectedResult = {'result': 'error: missing cube value'}
        parms = {'cube': ''}
        actualResult = check._validateEdges(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test220_920_CornerMissingCubeKey(self):
        expectedResult = {'error': 'error: missing cube key'}
        parms = {}
        actualResult = check._validateEdges(parms)
        self.assertDictEqual(expectedResult, actualResult)