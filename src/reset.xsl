<xsl:stylesheet version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes" 
    standalone="no" omit-xml-declaration="no"/>
  
  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>
  
  <xsl:template match="STATUS-LIST/FIELD[@GROUP='DAILY_EXPORT']/@VALUE">
    <xsl:attribute name="VALUE">NO</xsl:attribute>
  </xsl:template>
  
</xsl:stylesheet>
