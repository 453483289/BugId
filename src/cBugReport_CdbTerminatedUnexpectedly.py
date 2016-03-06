from mHTML import sDetailsHTMLTemplate, fsHTMLEncode;

class cBugReport_CdbTerminatedUnexpectedly(object):
  def __init__(oBugReport, oCdbWrapper, uExitCode):
    oBugReport.sBugTypeId = "CdbTerminated:%d" % uExitCode;
    oBugReport.sBugDescription = "Cdb terminated unexpectedly";
    oBugReport.sBugLocation = None;
    oBugReport.sSecurityImpact = None;
    oBugReport.oException = None;
    oBugReport.oStack = None;
    
    oBugReport.sImportantOutputHTML = oCdbWrapper.sImportantOutputHTML;
    oBugReport.sProcessBinaryName = "cdb.exe";
    
    oBugReport.sId = oBugReport.sBugTypeId;
    oBugReport.sStackId = None;
    oBugReport.sBugLocation = None;
    
    # Turn cdb output into formatted HTML. It is separated into blocks, one for the initial cdb output and one for each
    # command executed.
    sCdbStdIOHTML = '<hr/>'.join(oCdbWrapper.asCdbStdIOBlocksHTML);
    del oCdbWrapper.asHTMLCdbStdIOBlocks;
    # Create HTML details
    oBugReport.sHTMLDetails = sDetailsHTMLTemplate % {
      "sId": fsHTMLEncode(oBugReport.sId),
      "sBugDescription": fsHTMLEncode(oBugReport.sBugDescription),
      "sBugLocation": fsHTMLEncode(oBugReport.sBugLocation or "Unknown"),
      "sSecurityImpact": oBugReport.sSecurityImpact and \
            '<span class="SecurityImpact">%s</span>' % fsHTMLEncode(oBugReport.sSecurityImpact) or "None",
      "sOptionalBlocks": "",
      "sCdbStdIO": sCdbStdIOHTML,
    };
