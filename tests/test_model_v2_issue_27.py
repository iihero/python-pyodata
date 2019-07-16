"""Tests for OData Model module"""
# pylint: disable=line-too-long,too-many-locals,too-many-statements

from datetime import datetime
import pytest
from pyodata.v2.model import Edmx

def test_parse(schema):
    """Test Edmx class"""

    schema = Edmx.parse("""<edmx:Edmx xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx" Version="4.0">
  <edmx:DataServices>
    <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="ODataService">
      <EntityType Name="Office">
        <Key>
          <PropertyRef Name="OfficeKey"/>
        </Key>
        <Property Name="BridgeModificationTimestamp" Type="Edm.DateTimeOffset" Precision="27">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="Media" Type="ODataService.Media">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="FranchiseAffiliation" Type="Edm.String" MaxLength="50"/>
        <Property Name="IDXOfficeParticipationYN" Type="Edm.Boolean"/>
        <Property Name="MainOfficeKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="MainOfficeKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="MainOfficeMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="ModificationTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OfficeAOR" Type="OfficeEnums.OfficeAOR" MaxLength="50"/>
        <Property Name="OfficeAORMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="OfficeAORkey" Type="Edm.String" MaxLength="255"/>
        <Property Name="OfficeAORkeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="OfficeAddress1" Type="Edm.String" MaxLength="50"/>
        <Property Name="OfficeAddress2" Type="Edm.String" MaxLength="50"/>
        <Property Name="OfficeAssociationComments" Type="Edm.String" MaxLength="500"/>
        <Property Name="OfficeBranchType" Type="OfficeEnums.OfficeBranchType" MaxLength="50"/>
        <Property Name="OfficeBrokerKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="OfficeBrokerKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="OfficeBrokerMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="OfficeCity" Type="Edm.String" MaxLength="50"/>
        <Property Name="OfficeCorporateLicense" Type="Edm.String" MaxLength="50"/>
        <Property Name="OfficeCountyOrParish" Type="OfficeEnums.OfficeCountyOrParish" MaxLength="50"/>
        <Property Name="OfficeEmail" Type="Edm.String" MaxLength="80"/>
        <Property Name="OfficeFax" Type="Edm.String" MaxLength="16"/>
        <Property Name="OfficeKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="OfficeKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="OfficeManagerKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="OfficeManagerKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="OfficeManagerMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="OfficeMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="OfficeName" Type="Edm.String" MaxLength="255"/>
        <Property Name="OfficeNationalAssociationId" Type="Edm.String" MaxLength="25"/>
        <Property Name="OfficePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="OfficePhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="OfficePostalCode" Type="Edm.String" MaxLength="10"/>
        <Property Name="OfficePostalCodePlus4" Type="Edm.String" MaxLength="4"/>
        <Property Name="OfficeStateOrProvince" Type="OfficeEnums.OfficeStateOrProvince" MaxLength="2"/>
        <Property Name="OfficeStatus" Type="OfficeEnums.OfficeStatus" MaxLength="25"/>
        <Property Name="OfficeType" Type="OfficeEnums.OfficeType" MaxLength="50"/>
        <Property Name="OriginalEntryTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OriginatingSystemID" Type="Edm.String" MaxLength="25"/>
        <Property Name="OriginatingSystemName" Type="Edm.String" MaxLength="255"/>
        <Property Name="OriginatingSystemOfficeKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="SocialMediaType" Type="OfficeEnums.SocialMediaType" MaxLength="25"/>
        <Property Name="SourceSystemID" Type="Edm.String" MaxLength="25"/>
        <Property Name="SourceSystemName" Type="Edm.String" MaxLength="255"/>
        <Property Name="SourceSystemOfficeKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="SyndicateAgentOption" Type="OfficeEnums.SyndicateAgentOption" MaxLength="50"/>
        <Property Name="SyndicateTo" Type="OfficeEnums.SyndicateTo" MaxLength="1024"/>
      </EntityType>
      <EntityType Name="Member">
        <Key>
          <PropertyRef Name="MemberKey"/>
        </Key>
        <Property Name="BridgeModificationTimestamp" Type="Edm.DateTimeOffset" Precision="27">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="Media" Type="ODataService.Media">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="JobTitle" Type="Edm.String" MaxLength="50"/>
        <Property Name="LastLoginTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="MemberAOR" Type="MemberEnums.MemberAOR" MaxLength="50"/>
        <Property Name="MemberAORMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="MemberAORkey" Type="Edm.String" MaxLength="255"/>
        <Property Name="MemberAORkeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="MemberAddress1" Type="Edm.String" MaxLength="50"/>
        <Property Name="MemberAddress2" Type="Edm.String" MaxLength="50"/>
        <Property Name="MemberAssociationComments" Type="Edm.String" MaxLength="500"/>
        <Property Name="MemberCarrierRoute" Type="Edm.String" MaxLength="9"/>
        <Property Name="MemberCity" Type="Edm.String" MaxLength="50"/>
        <Property Name="MemberCountry" Type="MemberEnums.MemberCountry" MaxLength="2"/>
        <Property Name="MemberCountyOrParish" Type="MemberEnums.MemberCountyOrParish" MaxLength="50"/>
        <Property Name="MemberDesignation" Type="MemberEnums.MemberDesignation" MaxLength="50"/>
        <Property Name="MemberDirectPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="MemberEmail" Type="Edm.String" MaxLength="80"/>
        <Property Name="MemberFax" Type="Edm.String" MaxLength="16"/>
        <Property Name="MemberFirstName" Type="Edm.String" MaxLength="50"/>
        <Property Name="MemberFullName" Type="Edm.String" MaxLength="150"/>
        <Property Name="MemberHomePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="MemberIsAssistantTo" Type="Edm.String" MaxLength="50"/>
        <Property Name="MemberKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="MemberKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="MemberLanguages" Type="MemberEnums.MemberLanguages" MaxLength="1024"/>
        <Property Name="MemberLastName" Type="Edm.String" MaxLength="50"/>
        <Property Name="MemberLoginId" Type="Edm.String" MaxLength="25"/>
        <Property Name="MemberMiddleName" Type="Edm.String" MaxLength="50"/>
        <Property Name="MemberMlsAccessYN" Type="Edm.Boolean"/>
        <Property Name="MemberMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="MemberMlsSecurityClass" Type="MemberEnums.MemberMlsSecurityClass" MaxLength="25"/>
        <Property Name="MemberMobilePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="MemberNamePrefix" Type="Edm.String" MaxLength="10"/>
        <Property Name="MemberNameSuffix" Type="Edm.String" MaxLength="10"/>
        <Property Name="MemberNationalAssociationId" Type="Edm.String" MaxLength="25"/>
        <Property Name="MemberNickname" Type="Edm.String" MaxLength="50"/>
        <Property Name="MemberOtherPhoneType" Type="MemberEnums.MemberOtherPhoneType" MaxLength="25"/>
        <Property Name="MemberOfficePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="MemberOfficePhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="MemberPager" Type="Edm.String" MaxLength="16"/>
        <Property Name="MemberPassword" Type="Edm.String" MaxLength="25"/>
        <Property Name="MemberPhoneTTYTDD" Type="Edm.String" MaxLength="16"/>
        <Property Name="MemberPostalCode" Type="Edm.String" MaxLength="10"/>
        <Property Name="MemberPostalCodePlus4" Type="Edm.String" MaxLength="4"/>
        <Property Name="MemberPreferredPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="MemberPreferredPhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="MemberStateLicense" Type="Edm.String" MaxLength="50"/>
        <Property Name="MemberStateLicenseState" Type="MemberEnums.MemberStateLicenseState" MaxLength="2"/>
        <Property Name="MemberStateOrProvince" Type="MemberEnums.MemberStateOrProvince" MaxLength="2"/>
        <Property Name="MemberStatus" Type="MemberEnums.MemberStatus" MaxLength="25"/>
        <Property Name="MemberTollFreePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="MemberType" Type="MemberEnums.MemberType" MaxLength="25"/>
        <Property Name="MemberVoiceMail" Type="Edm.String" MaxLength="16"/>
        <Property Name="MemberVoiceMailExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="ModificationTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OfficeKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="OfficeKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="OfficeMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="OfficeName" Type="Edm.String" MaxLength="255"/>
        <Property Name="OriginalEntryTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OriginatingSystemID" Type="Edm.String" MaxLength="25"/>
        <Property Name="OriginatingSystemMemberKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="OriginatingSystemName" Type="Edm.String" MaxLength="255"/>
        <Property Name="SocialMediaType" Type="MemberEnums.SocialMediaType" MaxLength="25"/>
        <Property Name="SourceSystemID" Type="Edm.String" MaxLength="25"/>
        <Property Name="SourceSystemMemberKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="SourceSystemName" Type="Edm.String" MaxLength="255"/>
        <Property Name="SyndicateTo" Type="MemberEnums.SyndicateTo" MaxLength="1024"/>
      </EntityType>
      <EntityType Name="Property">
        <Key>
          <PropertyRef Name="ListingKey"/>
        </Key>
        <Property Name="BridgeModificationTimestamp" Type="Edm.DateTimeOffset" Precision="27">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="IDXParticipationYN" Type="Edm.Boolean">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="MaloneId" Type="Edm.Int64" Precision="255">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="Media" Type="ODataService.Media">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="ListingInputOriginalMedia" Type="ODataService.ListingInputOriginalMedia">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="VirtualTourURLZillow" Type="Edm.String" MaxLength="8000">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="AboveGradeFinishedArea" Type="Edm.Double" Precision="14"/>
        <Property Name="AboveGradeFinishedAreaSource" Type="PropertyEnums.AboveGradeFinishedAreaSource" MaxLength="50"/>
        <Property Name="AboveGradeFinishedAreaUnits" Type="PropertyEnums.AboveGradeFinishedAreaUnits" MaxLength="25"/>
        <Property Name="AccessCode" Type="Edm.String" MaxLength="25"/>
        <Property Name="AccessibilityFeatures" Type="PropertyEnums.AccessibilityFeatures" MaxLength="1024"/>
        <Property Name="AdditionalParcelsDescription" Type="Edm.String" MaxLength="255"/>
        <Property Name="AdditionalParcelsYN" Type="Edm.Boolean"/>
        <Property Name="AnchorsCoTenants" Type="Edm.String" MaxLength="1024"/>
        <Property Name="Appliances" Type="PropertyEnums.Appliances" MaxLength="1024"/>
        <Property Name="ArchitecturalStyle" Type="PropertyEnums.ArchitecturalStyle" MaxLength="1024"/>
        <Property Name="AssociationAmenities" Type="PropertyEnums.AssociationAmenities" MaxLength="1024"/>
        <Property Name="AssociationFee" Type="Edm.Double" Precision="14"/>
        <Property Name="AssociationFee2" Type="Edm.Double" Precision="14"/>
        <Property Name="AssociationFee2Frequency" Type="PropertyEnums.AssociationFee2Frequency" MaxLength="25"/>
        <Property Name="AssociationFeeFrequency" Type="PropertyEnums.AssociationFeeFrequency" MaxLength="25"/>
        <Property Name="AssociationFeeIncludes" Type="PropertyEnums.AssociationFeeIncludes" MaxLength="1024"/>
        <Property Name="AssociationName" Type="Edm.String" MaxLength="50"/>
        <Property Name="AssociationName2" Type="Edm.String" MaxLength="50"/>
        <Property Name="AssociationPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="AssociationPhone2" Type="Edm.String" MaxLength="16"/>
        <Property Name="AssociationYN" Type="Edm.Boolean"/>
        <Property Name="AttachedGarageYN" Type="Edm.Boolean"/>
        <Property Name="AvailabilityDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="Basement" Type="PropertyEnums.Basement" MaxLength="1024"/>
        <Property Name="BathroomsFull" Type="Edm.Int64" Precision="3"/>
        <Property Name="BathroomsHalf" Type="Edm.Int64" Precision="3"/>
        <Property Name="BathroomsOneQuarter" Type="Edm.Int64" Precision="3"/>
        <Property Name="BathroomsPartial" Type="Edm.Int64" Precision="3"/>
        <Property Name="BathroomsThreeQuarter" Type="Edm.Int64" Precision="3"/>
        <Property Name="BathroomsTotalInteger" Type="Edm.Int64" Precision="3"/>
        <Property Name="BathroomsTotalDecimal" Type="Edm.Double" Precision="5">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="BedroomsPossible" Type="Edm.Int64" Precision="3"/>
        <Property Name="BedroomsTotal" Type="Edm.Int64" Precision="3"/>
        <Property Name="BelowGradeFinishedArea" Type="Edm.Double" Precision="14"/>
        <Property Name="BelowGradeFinishedAreaSource" Type="PropertyEnums.BelowGradeFinishedAreaSource" MaxLength="50"/>
        <Property Name="BelowGradeFinishedAreaUnits" Type="PropertyEnums.BelowGradeFinishedAreaUnits" MaxLength="25"/>
        <Property Name="BodyType" Type="PropertyEnums.BodyType" MaxLength="1024"/>
        <Property Name="BuilderModel" Type="Edm.String" MaxLength="50"/>
        <Property Name="BuilderName" Type="Edm.String" MaxLength="50"/>
        <Property Name="BuildingAreaSource" Type="PropertyEnums.BuildingAreaSource" MaxLength="50"/>
        <Property Name="BuildingAreaTotal" Type="Edm.Double" Precision="14"/>
        <Property Name="BuildingAreaUnits" Type="PropertyEnums.BuildingAreaUnits" MaxLength="25"/>
        <Property Name="BuildingFeatures" Type="PropertyEnums.BuildingFeatures" MaxLength="1024"/>
        <Property Name="BuildingName" Type="Edm.String" MaxLength="50"/>
        <Property Name="BusinessName" Type="Edm.String" MaxLength="255"/>
        <Property Name="BusinessType" Type="PropertyEnums.BusinessType" MaxLength="1024"/>
        <Property Name="BuyerAgencyCompensation" Type="Edm.String" MaxLength="25"/>
        <Property Name="BuyerAgencyCompensationType" Type="PropertyEnums.BuyerAgencyCompensationType" MaxLength="25"/>
        <Property Name="BuyerAgentAOR" Type="PropertyEnums.BuyerAgentAOR" MaxLength="50"/>
        <Property Name="BuyerAgentDesignation" Type="PropertyEnums.BuyerAgentDesignation" MaxLength="50"/>
        <Property Name="BuyerAgentDirectPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerAgentEmail" Type="Edm.String" MaxLength="80"/>
        <Property Name="BuyerAgentFax" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerAgentFirstName" Type="Edm.String" MaxLength="50"/>
        <Property Name="BuyerAgentFullName" Type="Edm.String" MaxLength="150"/>
        <Property Name="BuyerAgentHomePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerAgentKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="BuyerAgentKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="BuyerAgentLastName" Type="Edm.String" MaxLength="50"/>
        <Property Name="BuyerAgentMiddleName" Type="Edm.String" MaxLength="50"/>
        <Property Name="BuyerAgentMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="BuyerAgentMobilePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerAgentNamePrefix" Type="Edm.String" MaxLength="10"/>
        <Property Name="BuyerAgentNameSuffix" Type="Edm.String" MaxLength="10"/>
        <Property Name="BuyerAgentOfficePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerAgentOfficePhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="BuyerAgentPager" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerAgentPreferredPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerAgentPreferredPhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="BuyerAgentStateLicense" Type="Edm.String" MaxLength="50"/>
        <Property Name="BuyerAgentTollFreePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerAgentURL" Type="Edm.String" MaxLength="8000"/>
        <Property Name="BuyerAgentVoiceMail" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerAgentVoiceMailExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="BuyerFinancing" Type="PropertyEnums.BuyerFinancing" MaxLength="1024"/>
        <Property Name="BuyerOfficeAOR" Type="PropertyEnums.BuyerOfficeAOR" MaxLength="50"/>
        <Property Name="BuyerOfficeEmail" Type="Edm.String" MaxLength="80"/>
        <Property Name="BuyerOfficeFax" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerOfficeKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="BuyerOfficeKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="BuyerOfficeMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="BuyerOfficeName" Type="Edm.String" MaxLength="255"/>
        <Property Name="BuyerOfficePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="BuyerOfficePhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="BuyerOfficeURL" Type="Edm.String" MaxLength="8000"/>
        <Property Name="BuyerTeamKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="BuyerTeamKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="BuyerTeamName" Type="Edm.String" MaxLength="50"/>
        <Property Name="CableTvExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="CancelationDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="CapRate" Type="Edm.Double" Precision="5"/>
        <Property Name="CarportSpaces" Type="Edm.Double" Precision="14"/>
        <Property Name="CarportYN" Type="Edm.Boolean"/>
        <Property Name="CarrierRoute" Type="Edm.String" MaxLength="9"/>
        <Property Name="City" Type="PropertyEnums.City" MaxLength="50"/>
        <Property Name="CityRegion" Type="Edm.String" MaxLength="150"/>
        <Property Name="CloseDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="ClosePrice" Type="Edm.Double" Precision="14"/>
        <Property Name="CoBuyerAgentAOR" Type="PropertyEnums.CoBuyerAgentAOR" MaxLength="50"/>
        <Property Name="CoBuyerAgentDesignation" Type="PropertyEnums.CoBuyerAgentDesignation" MaxLength="50"/>
        <Property Name="CoBuyerAgentDirectPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerAgentEmail" Type="Edm.String" MaxLength="80"/>
        <Property Name="CoBuyerAgentFax" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerAgentFirstName" Type="Edm.String" MaxLength="50"/>
        <Property Name="CoBuyerAgentFullName" Type="Edm.String" MaxLength="150"/>
        <Property Name="CoBuyerAgentHomePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerAgentKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="CoBuyerAgentKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="CoBuyerAgentLastName" Type="Edm.String" MaxLength="50"/>
        <Property Name="CoBuyerAgentMiddleName" Type="Edm.String" MaxLength="50"/>
        <Property Name="CoBuyerAgentMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="CoBuyerAgentMobilePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerAgentNamePrefix" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoBuyerAgentNameSuffix" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoBuyerAgentOfficePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerAgentOfficePhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoBuyerAgentPager" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerAgentPreferredPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerAgentPreferredPhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoBuyerAgentStateLicense" Type="Edm.String" MaxLength="50"/>
        <Property Name="CoBuyerAgentTollFreePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerAgentURL" Type="Edm.String" MaxLength="8000"/>
        <Property Name="CoBuyerAgentVoiceMail" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerAgentVoiceMailExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoBuyerOfficeAOR" Type="PropertyEnums.CoBuyerOfficeAOR" MaxLength="50"/>
        <Property Name="CoBuyerOfficeEmail" Type="Edm.String" MaxLength="80"/>
        <Property Name="CoBuyerOfficeFax" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerOfficeKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="CoBuyerOfficeKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="CoBuyerOfficeMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="CoBuyerOfficeName" Type="Edm.String" MaxLength="255"/>
        <Property Name="CoBuyerOfficePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoBuyerOfficePhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoBuyerOfficeURL" Type="Edm.String" MaxLength="8000"/>
        <Property Name="CoListAgentAOR" Type="PropertyEnums.CoListAgentAOR" MaxLength="50"/>
        <Property Name="CoListAgentDesignation" Type="PropertyEnums.CoListAgentDesignation" MaxLength="50"/>
        <Property Name="CoListAgentDirectPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListAgentEmail" Type="Edm.String" MaxLength="80"/>
        <Property Name="CoListAgentFax" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListAgentFirstName" Type="Edm.String" MaxLength="50"/>
        <Property Name="CoListAgentFullName" Type="Edm.String" MaxLength="150"/>
        <Property Name="CoListAgentHomePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListAgentKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="CoListAgentKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="CoListAgentLastName" Type="Edm.String" MaxLength="50"/>
        <Property Name="CoListAgentMiddleName" Type="Edm.String" MaxLength="50"/>
        <Property Name="CoListAgentMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="CoListAgentMobilePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListAgentNamePrefix" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoListAgentNameSuffix" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoListAgentOfficePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListAgentOfficePhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoListAgentPager" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListAgentPreferredPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListAgentPreferredPhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoListAgentStateLicense" Type="Edm.String" MaxLength="50"/>
        <Property Name="CoListAgentTollFreePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListAgentURL" Type="Edm.String" MaxLength="8000"/>
        <Property Name="CoListAgentVoiceMail" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListAgentVoiceMailExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoListOfficeAOR" Type="PropertyEnums.CoListOfficeAOR" MaxLength="50"/>
        <Property Name="CoListOfficeEmail" Type="Edm.String" MaxLength="80"/>
        <Property Name="CoListOfficeFax" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListOfficeKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="CoListOfficeKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="CoListOfficeMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="CoListOfficeName" Type="Edm.String" MaxLength="255"/>
        <Property Name="CoListOfficePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="CoListOfficePhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="CoListOfficeURL" Type="Edm.String" MaxLength="8000"/>
        <Property Name="CommonInterest" Type="PropertyEnums.CommonInterest" MaxLength="25"/>
        <Property Name="CommonWalls" Type="PropertyEnums.CommonWalls" MaxLength="1024"/>
        <Property Name="CommunityFeatures" Type="PropertyEnums.CommunityFeatures" MaxLength="1024"/>
        <Property Name="Concessions" Type="PropertyEnums.Concessions" MaxLength="25"/>
        <Property Name="ConcessionsAmount" Type="Edm.Int64" Precision="11"/>
        <Property Name="ConcessionsComments" Type="Edm.String" MaxLength="200"/>
        <Property Name="ConstructionMaterials" Type="PropertyEnums.ConstructionMaterials" MaxLength="1024"/>
        <Property Name="ContinentRegion" Type="Edm.String" MaxLength="150"/>
        <Property Name="Contingency" Type="Edm.String" MaxLength="1024"/>
        <Property Name="ContingentDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="ContractStatusChangeDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="Cooling" Type="PropertyEnums.Cooling" MaxLength="1024"/>
        <Property Name="CoolingYN" Type="Edm.Boolean"/>
        <Property Name="Coordinates" Type="Edm.GeographyPoint">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="CopyrightNotice" Type="Edm.String" MaxLength="500"/>
        <Property Name="Country" Type="PropertyEnums.Country" MaxLength="2"/>
        <Property Name="CountryRegion" Type="Edm.String" MaxLength="150"/>
        <Property Name="CountyOrParish" Type="PropertyEnums.CountyOrParish" MaxLength="50"/>
        <Property Name="CoveredSpaces" Type="Edm.Double" Precision="14"/>
        <Property Name="CropsIncludedYN" Type="Edm.Boolean"/>
        <Property Name="CrossStreet" Type="Edm.String" MaxLength="50"/>
        <Property Name="CultivatedArea" Type="Edm.Double" Precision="14"/>
        <Property Name="CumulativeDaysOnMarket" Type="Edm.Int64" Precision="4"/>
        <Property Name="CurrentFinancing" Type="PropertyEnums.CurrentFinancing" MaxLength="1024"/>
        <Property Name="CurrentUse" Type="PropertyEnums.CurrentUse" MaxLength="1024"/>
        <Property Name="DOH1" Type="Edm.String" MaxLength="25"/>
        <Property Name="DOH2" Type="Edm.String" MaxLength="25"/>
        <Property Name="DOH3" Type="Edm.String" MaxLength="25"/>
        <Property Name="DaysOnMarket" Type="Edm.Int64" Precision="4"/>
        <Property Name="DevelopmentStatus" Type="PropertyEnums.DevelopmentStatus" MaxLength="1024"/>
        <Property Name="DirectionFaces" Type="PropertyEnums.DirectionFaces" MaxLength="25"/>
        <Property Name="Directions" Type="Edm.String" MaxLength="1024"/>
        <Property Name="Disclaimer" Type="Edm.String" MaxLength="500"/>
        <Property Name="Disclosures" Type="PropertyEnums.Disclosures" MaxLength="4000"/>
        <Property Name="DistanceToBusComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToBusNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToBusUnits" Type="PropertyEnums.DistanceToBusUnits" MaxLength="25"/>
        <Property Name="DistanceToElectricComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToElectricNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToElectricUnits" Type="PropertyEnums.DistanceToElectricUnits" MaxLength="25"/>
        <Property Name="DistanceToFreewayComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToFreewayNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToFreewayUnits" Type="PropertyEnums.DistanceToFreewayUnits" MaxLength="25"/>
        <Property Name="DistanceToGasComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToGasNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToGasUnits" Type="PropertyEnums.DistanceToGasUnits" MaxLength="25"/>
        <Property Name="DistanceToPhoneServiceComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToPhoneServiceNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToPhoneServiceUnits" Type="PropertyEnums.DistanceToPhoneServiceUnits" MaxLength="25"/>
        <Property Name="DistanceToPlaceofWorshipComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToPlaceofWorshipNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToPlaceofWorshipUnits" Type="PropertyEnums.DistanceToPlaceofWorshipUnits" MaxLength="25"/>
        <Property Name="DistanceToSchoolBusComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToSchoolBusNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToSchoolBusUnits" Type="PropertyEnums.DistanceToSchoolBusUnits" MaxLength="25"/>
        <Property Name="DistanceToSchoolsComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToSchoolsNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToSchoolsUnits" Type="PropertyEnums.DistanceToSchoolsUnits" MaxLength="25"/>
        <Property Name="DistanceToSewerComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToSewerNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToSewerUnits" Type="PropertyEnums.DistanceToSewerUnits" MaxLength="25"/>
        <Property Name="DistanceToShoppingComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToShoppingNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToShoppingUnits" Type="PropertyEnums.DistanceToShoppingUnits" MaxLength="25"/>
        <Property Name="DistanceToStreetComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToStreetNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToStreetUnits" Type="PropertyEnums.DistanceToStreetUnits" MaxLength="25"/>
        <Property Name="DistanceToWaterComments" Type="Edm.String" MaxLength="255"/>
        <Property Name="DistanceToWaterNumeric" Type="Edm.Int64" Precision="16"/>
        <Property Name="DistanceToWaterUnits" Type="PropertyEnums.DistanceToWaterUnits" MaxLength="25"/>
        <Property Name="DocumentsAvailable" Type="PropertyEnums.DocumentsAvailable" MaxLength="1024"/>
        <Property Name="DocumentsChangeTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="DocumentsCount" Type="Edm.Int64" Precision="2"/>
        <Property Name="DoorFeatures" Type="PropertyEnums.DoorFeatures" MaxLength="1024"/>
        <Property Name="DualVariableCompensationYN" Type="Edm.Boolean"/>
        <Property Name="Electric" Type="PropertyEnums.Electric" MaxLength="1024"/>
        <Property Name="ElectricExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="ElectricOnPropertyYN" Type="Edm.Boolean"/>
        <Property Name="ElementarySchool" Type="PropertyEnums.ElementarySchool" MaxLength="50"/>
        <Property Name="ElementarySchoolDistrict" Type="PropertyEnums.ElementarySchoolDistrict" MaxLength="50"/>
        <Property Name="Elevation" Type="Edm.Int64" Precision="5"/>
        <Property Name="ElevationUnits" Type="PropertyEnums.ElevationUnits" MaxLength="10"/>
        <Property Name="EntryLevel" Type="Edm.Int64" Precision="4"/>
        <Property Name="EntryLocation" Type="Edm.String" MaxLength="50"/>
        <Property Name="Exclusions" Type="Edm.String" MaxLength="1024"/>
        <Property Name="ExistingLeaseType" Type="PropertyEnums.ExistingLeaseType" MaxLength="75"/>
        <Property Name="ExpirationDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="ExteriorFeatures" Type="PropertyEnums.ExteriorFeatures" MaxLength="1024"/>
        <Property Name="FarmCreditServiceInclYN" Type="Edm.Boolean"/>
        <Property Name="FarmLandAreaSource" Type="PropertyEnums.FarmLandAreaSource" MaxLength="50"/>
        <Property Name="FarmLandAreaUnits" Type="PropertyEnums.FarmLandAreaUnits" MaxLength="25"/>
        <Property Name="Fencing" Type="PropertyEnums.Fencing" MaxLength="1024"/>
        <Property Name="FinancialDataSource" Type="PropertyEnums.FinancialDataSource" MaxLength="75"/>
        <Property Name="FireplaceFeatures" Type="PropertyEnums.FireplaceFeatures" MaxLength="1024"/>
        <Property Name="FireplaceYN" Type="Edm.Boolean"/>
        <Property Name="FireplacesTotal" Type="Edm.Int64" Precision="3"/>
        <Property Name="Flooring" Type="PropertyEnums.Flooring" MaxLength="1024"/>
        <Property Name="FoundationArea" Type="Edm.Double" Precision="14"/>
        <Property Name="FoundationDetails" Type="PropertyEnums.FoundationDetails" MaxLength="1024"/>
        <Property Name="FrontageLength" Type="Edm.String" MaxLength="255"/>
        <Property Name="FrontageType" Type="PropertyEnums.FrontageType" MaxLength="1024"/>
        <Property Name="FuelExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="Furnished" Type="PropertyEnums.Furnished" MaxLength="50"/>
        <Property Name="FurnitureReplacementExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="GarageSpaces" Type="Edm.Double" Precision="14"/>
        <Property Name="GarageYN" Type="Edm.Boolean"/>
        <Property Name="GardenerExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="GrazingPermitsBlmYN" Type="Edm.Boolean"/>
        <Property Name="GrazingPermitsForestServiceYN" Type="Edm.Boolean"/>
        <Property Name="GrazingPermitsPrivateYN" Type="Edm.Boolean"/>
        <Property Name="GreenBuildingVerificationType" Type="PropertyEnums.GreenBuildingVerificationType" MaxLength="1024"/>
        <Property Name="GreenEnergyEfficient" Type="PropertyEnums.GreenEnergyEfficient" MaxLength="1024"/>
        <Property Name="GreenEnergyGeneration" Type="PropertyEnums.GreenEnergyGeneration" MaxLength="1024"/>
        <Property Name="GreenIndoorAirQuality" Type="PropertyEnums.GreenIndoorAirQuality" MaxLength="1024"/>
        <Property Name="GreenLocation" Type="PropertyEnums.GreenLocation" MaxLength="1024"/>
        <Property Name="GreenSustainability" Type="PropertyEnums.GreenSustainability" MaxLength="1024"/>
        <Property Name="GreenWaterConservation" Type="PropertyEnums.GreenWaterConservation" MaxLength="1024"/>
        <Property Name="GrossIncome" Type="Edm.Double" Precision="14"/>
        <Property Name="GrossScheduledIncome" Type="Edm.Double" Precision="14"/>
        <Property Name="HabitableResidenceYN" Type="Edm.Boolean"/>
        <Property Name="Heating" Type="PropertyEnums.Heating" MaxLength="1024"/>
        <Property Name="HeatingYN" Type="Edm.Boolean"/>
        <Property Name="HighSchool" Type="PropertyEnums.HighSchool" MaxLength="50"/>
        <Property Name="HighSchoolDistrict" Type="PropertyEnums.HighSchoolDistrict" MaxLength="50"/>
        <Property Name="HomeWarrantyYN" Type="Edm.Boolean"/>
        <Property Name="HorseAmenities" Type="PropertyEnums.HorseAmenities" MaxLength="1024"/>
        <Property Name="HorseYN" Type="Edm.Boolean"/>
        <Property Name="HoursDaysOfOperation" Type="PropertyEnums.HoursDaysOfOperation" MaxLength="1024"/>
        <Property Name="HoursDaysOfOperationDescription" Type="Edm.String" MaxLength="255"/>
        <Property Name="Inclusions" Type="Edm.String" MaxLength="1024"/>
        <Property Name="IncomeIncludes" Type="PropertyEnums.IncomeIncludes" MaxLength="1024"/>
        <Property Name="InsuranceExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="InteriorFeatures" Type="PropertyEnums.InteriorFeatures" MaxLength="1024"/>
        <Property Name="InternetAddressDisplayYN" Type="Edm.Boolean"/>
        <Property Name="InternetAutomatedValuationDisplayYN" Type="Edm.Boolean"/>
        <Property Name="InternetConsumerCommentYN" Type="Edm.Boolean"/>
        <Property Name="InternetEntireListingDisplayYN" Type="Edm.Boolean"/>
        <Property Name="IrrigationSource" Type="PropertyEnums.IrrigationSource" MaxLength="1024"/>
        <Property Name="IrrigationWaterRightsAcres" Type="Edm.Double" Precision="16"/>
        <Property Name="IrrigationWaterRightsYN" Type="Edm.Boolean"/>
        <Property Name="LaborInformation" Type="PropertyEnums.LaborInformation" MaxLength="1024"/>
        <Property Name="LandLeaseAmount" Type="Edm.Double" Precision="14"/>
        <Property Name="LandLeaseAmountFrequency" Type="PropertyEnums.LandLeaseAmountFrequency" MaxLength="25"/>
        <Property Name="LandLeaseExpirationDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="LandLeaseYN" Type="Edm.Boolean"/>
        <Property Name="Latitude" Type="Edm.Double" Precision="12"/>
        <Property Name="LaundryFeatures" Type="PropertyEnums.LaundryFeatures" MaxLength="1024"/>
        <Property Name="LeasableArea" Type="Edm.Double" Precision="14"/>
        <Property Name="LeasableAreaUnits" Type="PropertyEnums.LeasableAreaUnits" MaxLength="25"/>
        <Property Name="LeaseAmount" Type="Edm.Double" Precision="14"/>
        <Property Name="LeaseAmountFrequency" Type="PropertyEnums.LeaseAmountFrequency" MaxLength="25"/>
        <Property Name="LeaseAssignableYN" Type="Edm.Boolean"/>
        <Property Name="LeaseConsideredYN" Type="Edm.Boolean"/>
        <Property Name="LeaseExpiration" Type="Edm.Date" MaxLength="10"/>
        <Property Name="LeaseRenewalCompensation" Type="PropertyEnums.LeaseRenewalCompensation" MaxLength="255"/>
        <Property Name="LeaseRenewalOptionYN" Type="Edm.Boolean"/>
        <Property Name="LeaseTerm" Type="PropertyEnums.LeaseTerm" MaxLength="25"/>
        <Property Name="Levels" Type="PropertyEnums.Levels" MaxLength="1024"/>
        <Property Name="License1" Type="Edm.String" MaxLength="25"/>
        <Property Name="License2" Type="Edm.String" MaxLength="25"/>
        <Property Name="License3" Type="Edm.String" MaxLength="25"/>
        <Property Name="LicensesExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="ListAOR" Type="PropertyEnums.ListAOR" MaxLength="50"/>
        <Property Name="ListAgentAOR" Type="PropertyEnums.ListAgentAOR" MaxLength="50"/>
        <Property Name="ListAgentDesignation" Type="PropertyEnums.ListAgentDesignation" MaxLength="50"/>
        <Property Name="ListAgentDirectPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListAgentEmail" Type="Edm.String" MaxLength="80"/>
        <Property Name="ListAgentFax" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListAgentFirstName" Type="Edm.String" MaxLength="50"/>
        <Property Name="ListAgentFullName" Type="Edm.String" MaxLength="150"/>
        <Property Name="ListAgentHomePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListAgentKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="ListAgentKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="ListAgentLastName" Type="Edm.String" MaxLength="50"/>
        <Property Name="ListAgentMiddleName" Type="Edm.String" MaxLength="50"/>
        <Property Name="ListAgentMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="ListAgentMobilePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListAgentNamePrefix" Type="Edm.String" MaxLength="10"/>
        <Property Name="ListAgentNameSuffix" Type="Edm.String" MaxLength="10"/>
        <Property Name="ListAgentOfficePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListAgentOfficePhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="ListAgentPager" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListAgentPreferredPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListAgentPreferredPhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="ListAgentStateLicense" Type="Edm.String" MaxLength="50"/>
        <Property Name="ListAgentTollFreePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListAgentURL" Type="Edm.String" MaxLength="8000"/>
        <Property Name="ListAgentVoiceMail" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListAgentVoiceMailExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="ListOfficeAOR" Type="PropertyEnums.ListOfficeAOR" MaxLength="50"/>
        <Property Name="ListOfficeEmail" Type="Edm.String" MaxLength="80"/>
        <Property Name="ListOfficeFax" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListOfficeKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="ListOfficeKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="ListOfficeMlsId" Type="Edm.String" MaxLength="25"/>
        <Property Name="ListOfficeName" Type="Edm.String" MaxLength="255"/>
        <Property Name="ListOfficePhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="ListOfficePhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="ListOfficeURL" Type="Edm.String" MaxLength="8000"/>
        <Property Name="ListPrice" Type="Edm.Double" Precision="14"/>
        <Property Name="ListPriceLow" Type="Edm.Double" Precision="14"/>
        <Property Name="ListTeamKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="ListTeamKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="ListTeamName" Type="Edm.String" MaxLength="50"/>
        <Property Name="ListingAgreement" Type="PropertyEnums.ListingAgreement" MaxLength="25"/>
        <Property Name="ListingContractDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="ListingId" Type="Edm.String" MaxLength="255"/>
        <Property Name="ListingKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="ListingKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="ListingService" Type="PropertyEnums.ListingService" MaxLength="25"/>
        <Property Name="ListingTerms" Type="PropertyEnums.ListingTerms" MaxLength="1024"/>
        <Property Name="LivingArea" Type="Edm.Double" Precision="14"/>
        <Property Name="LivingAreaSource" Type="PropertyEnums.LivingAreaSource" MaxLength="50"/>
        <Property Name="LivingAreaUnits" Type="PropertyEnums.LivingAreaUnits" MaxLength="25"/>
        <Property Name="LockBoxLocation" Type="Edm.String" MaxLength="255"/>
        <Property Name="LockBoxSerialNumber" Type="Edm.String" MaxLength="25"/>
        <Property Name="LockBoxType" Type="PropertyEnums.LockBoxType" MaxLength="1024"/>
        <Property Name="Longitude" Type="Edm.Double" Precision="12"/>
        <Property Name="LotDimensionsSource" Type="PropertyEnums.LotDimensionsSource" MaxLength="50"/>
        <Property Name="LotFeatures" Type="PropertyEnums.LotFeatures" MaxLength="1024"/>
        <Property Name="LotSizeAcres" Type="Edm.Double" Precision="16"/>
        <Property Name="LotSizeArea" Type="Edm.Double" Precision="16"/>
        <Property Name="LotSizeDimensions" Type="Edm.String" MaxLength="150"/>
        <Property Name="LotSizeSource" Type="PropertyEnums.LotSizeSource" MaxLength="50"/>
        <Property Name="LotSizeSquareFeet" Type="Edm.Double" Precision="14"/>
        <Property Name="LotSizeUnits" Type="PropertyEnums.LotSizeUnits" MaxLength="25"/>
        <Property Name="MLSAreaMajor" Type="PropertyEnums.MLSAreaMajor" MaxLength="50"/>
        <Property Name="MLSAreaMinor" Type="PropertyEnums.MLSAreaMinor" MaxLength="50"/>
        <Property Name="MainLevelBathrooms" Type="Edm.Int64" Precision="3"/>
        <Property Name="MainLevelBedrooms" Type="Edm.Int64" Precision="3"/>
        <Property Name="MaintenanceExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="MajorChangeTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="MajorChangeType" Type="PropertyEnums.MajorChangeType" MaxLength="255"/>
        <Property Name="Make" Type="Edm.String" MaxLength="50"/>
        <Property Name="ManagerExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="MapCoordinate" Type="Edm.String" MaxLength="25"/>
        <Property Name="MapCoordinateSource" Type="Edm.String" MaxLength="25"/>
        <Property Name="MapURL" Type="Edm.String" MaxLength="8000"/>
        <Property Name="MiddleOrJuniorSchool" Type="PropertyEnums.MiddleOrJuniorSchool" MaxLength="50"/>
        <Property Name="MiddleOrJuniorSchoolDistrict" Type="PropertyEnums.MiddleOrJuniorSchoolDistrict" MaxLength="50"/>
        <Property Name="MlsStatus" Type="PropertyEnums.MlsStatus" MaxLength="50"/>
        <Property Name="MobileDimUnits" Type="PropertyEnums.MobileDimUnits" MaxLength="25"/>
        <Property Name="MobileHomeRemainsYN" Type="Edm.Boolean"/>
        <Property Name="MobileLength" Type="Edm.Int64" Precision="4"/>
        <Property Name="MobileWidth" Type="Edm.Int64" Precision="4"/>
        <Property Name="Model" Type="Edm.String" MaxLength="50"/>
        <Property Name="ModificationTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="NetOperatingIncome" Type="Edm.Double" Precision="14"/>
        <Property Name="NewConstructionYN" Type="Edm.Boolean"/>
        <Property Name="NewTaxesExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="NumberOfBuildings" Type="Edm.Int64" Precision="3"/>
        <Property Name="NumberOfFullTimeEmployees" Type="Edm.Int64" Precision="10"/>
        <Property Name="NumberOfLots" Type="Edm.Int64" Precision="3"/>
        <Property Name="NumberOfPads" Type="Edm.Int64" Precision="3"/>
        <Property Name="NumberOfPartTimeEmployees" Type="Edm.Int64" Precision="10"/>
        <Property Name="NumberOfSeparateElectricMeters" Type="Edm.Int64" Precision="3"/>
        <Property Name="NumberOfSeparateGasMeters" Type="Edm.Int64" Precision="3"/>
        <Property Name="NumberOfSeparateWaterMeters" Type="Edm.Int64" Precision="3"/>
        <Property Name="NumberOfUnitsInCommunity" Type="Edm.Int64" Precision="5"/>
        <Property Name="NumberOfUnitsLeased" Type="Edm.Int64" Precision="5"/>
        <Property Name="NumberOfUnitsMoMo" Type="Edm.Int64" Precision="5"/>
        <Property Name="NumberOfUnitsTotal" Type="Edm.Int64" Precision="3"/>
        <Property Name="NumberOfUnitsVacant" Type="Edm.Int64" Precision="5"/>
        <Property Name="OccupantName" Type="Edm.String" MaxLength="50"/>
        <Property Name="OccupantPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="OccupantType" Type="PropertyEnums.OccupantType" MaxLength="50"/>
        <Property Name="OffMarketDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="OffMarketTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OnMarketDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="OnMarketTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OpenParkingSpaces" Type="Edm.Double" Precision="14"/>
        <Property Name="OpenParkingYN" Type="Edm.Boolean"/>
        <Property Name="OperatingExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="OperatingExpenseIncludes" Type="PropertyEnums.OperatingExpenseIncludes" MaxLength="1024"/>
        <Property Name="OriginalEntryTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OriginalListPrice" Type="Edm.Double" Precision="14"/>
        <Property Name="OriginatingSystemID" Type="Edm.String" MaxLength="25"/>
        <Property Name="OriginatingSystemKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="OriginatingSystemName" Type="Edm.String" MaxLength="255"/>
        <Property Name="OtherEquipment" Type="PropertyEnums.OtherEquipment" MaxLength="1024"/>
        <Property Name="OtherExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="OtherParking" Type="Edm.String" MaxLength="1024"/>
        <Property Name="OtherStructures" Type="PropertyEnums.OtherStructures" MaxLength="1024"/>
        <Property Name="OwnerName" Type="Edm.String" MaxLength="50"/>
        <Property Name="OwnerPays" Type="PropertyEnums.OwnerPays" MaxLength="1024"/>
        <Property Name="OwnerPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="Ownership" Type="Edm.String" MaxLength="1024"/>
        <Property Name="OwnershipType" Type="PropertyEnums.OwnershipType" MaxLength="50"/>
        <Property Name="ParcelNumber" Type="Edm.String" MaxLength="50"/>
        <Property Name="ParkManagerName" Type="Edm.String" MaxLength="50"/>
        <Property Name="ParkManagerPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="ParkName" Type="Edm.String" MaxLength="50"/>
        <Property Name="ParkingFeatures" Type="PropertyEnums.ParkingFeatures" MaxLength="1024"/>
        <Property Name="ParkingTotal" Type="Edm.Double" Precision="14"/>
        <Property Name="PastureArea" Type="Edm.Double" Precision="14"/>
        <Property Name="PatioAndPorchFeatures" Type="PropertyEnums.PatioAndPorchFeatures" MaxLength="1024"/>
        <Property Name="PendingTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="PestControlExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="PetsAllowed" Type="PropertyEnums.PetsAllowed" MaxLength="1024"/>
        <Property Name="PhotosChangeTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="PhotosCount" Type="Edm.Int64" Precision="2"/>
        <Property Name="PoolExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="PoolFeatures" Type="PropertyEnums.PoolFeatures" MaxLength="1024"/>
        <Property Name="PoolPrivateYN" Type="Edm.Boolean"/>
        <Property Name="Possession" Type="PropertyEnums.Possession" MaxLength="255"/>
        <Property Name="PossibleUse" Type="PropertyEnums.PossibleUse" MaxLength="1024"/>
        <Property Name="PostalCity" Type="PropertyEnums.PostalCity" MaxLength="50"/>
        <Property Name="PostalCode" Type="Edm.String" MaxLength="10"/>
        <Property Name="PostalCodePlus4" Type="Edm.String" MaxLength="4"/>
        <Property Name="PowerProductionType" Type="PropertyEnums.PowerProductionType" MaxLength="1024"/>
        <Property Name="PreviousListPrice" Type="Edm.Double" Precision="14"/>
        <Property Name="PriceChangeTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="PrivateOfficeRemarks" Type="Edm.String" MaxLength="4000"/>
        <Property Name="PrivateRemarks" Type="Edm.String" MaxLength="4000"/>
        <Property Name="ProfessionalManagementExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="PropertyAttachedYN" Type="Edm.Boolean"/>
        <Property Name="PropertyCondition" Type="PropertyEnums.PropertyCondition" MaxLength="1024"/>
        <Property Name="PropertySubType" Type="PropertyEnums.PropertySubType" MaxLength="50"/>
        <Property Name="PropertyType" Type="PropertyEnums.PropertyType" MaxLength="50"/>
        <Property Name="PublicRemarks" Type="Edm.String" MaxLength="4000"/>
        <Property Name="PublicSurveyRange" Type="Edm.String" MaxLength="20"/>
        <Property Name="PublicSurveySection" Type="Edm.String" MaxLength="20"/>
        <Property Name="PublicSurveyTownship" Type="Edm.String" MaxLength="20"/>
        <Property Name="PropertyUniversalID" Type="Edm.String" MaxLength="128"/>
        <Property Name="PurchaseContractDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="RVParkingDimensions" Type="Edm.String" MaxLength="50"/>
        <Property Name="RangeArea" Type="Edm.Double" Precision="14"/>
        <Property Name="RentControlYN" Type="Edm.Boolean"/>
        <Property Name="RentIncludes" Type="PropertyEnums.RentIncludes" MaxLength="1024"/>
        <Property Name="RoadFrontageType" Type="PropertyEnums.RoadFrontageType" MaxLength="1024"/>
        <Property Name="RoadResponsibility" Type="PropertyEnums.RoadResponsibility" MaxLength="1024"/>
        <Property Name="RoadSurfaceType" Type="PropertyEnums.RoadSurfaceType" MaxLength="1024"/>
        <Property Name="Roof" Type="PropertyEnums.Roof" MaxLength="1024"/>
        <Property Name="RoomsTotal" Type="Edm.Int64" Precision="3"/>
        <Property Name="RoomType" Type="PropertyEnums.RoomType" MaxLength="1024"/>
        <Property Name="SeatingCapacity" Type="Edm.Int64" Precision="10"/>
        <Property Name="SecurityFeatures" Type="PropertyEnums.SecurityFeatures" MaxLength="1024"/>
        <Property Name="SeniorCommunityYN" Type="Edm.Boolean"/>
        <Property Name="SerialU" Type="Edm.String" MaxLength="25"/>
        <Property Name="SerialX" Type="Edm.String" MaxLength="25"/>
        <Property Name="SerialXX" Type="Edm.String" MaxLength="25"/>
        <Property Name="Sewer" Type="PropertyEnums.Sewer" MaxLength="1024"/>
        <Property Name="ShowingAdvanceNotice" Type="Edm.Int64" Precision="2"/>
        <Property Name="ShowingAttendedYN" Type="Edm.Boolean"/>
        <Property Name="ShowingContactName" Type="Edm.String" MaxLength="40"/>
        <Property Name="ShowingContactPhone" Type="Edm.String" MaxLength="16"/>
        <Property Name="ShowingContactPhoneExt" Type="Edm.String" MaxLength="10"/>
        <Property Name="ShowingContactType" Type="PropertyEnums.ShowingContactType" MaxLength="75"/>
        <Property Name="ShowingDays" Type="PropertyEnums.ShowingDays" MaxLength="1024"/>
        <Property Name="ShowingEndTime" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="ShowingInstructions" Type="Edm.String" MaxLength="4000"/>
        <Property Name="ShowingRequirements" Type="PropertyEnums.ShowingRequirements" MaxLength="1024"/>
        <Property Name="ShowingStartTime" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="SignOnPropertyYN" Type="Edm.Boolean"/>
        <Property Name="Skirt" Type="PropertyEnums.Skirt" MaxLength="1024"/>
        <Property Name="SourceSystemID" Type="Edm.String" MaxLength="25"/>
        <Property Name="SourceSystemKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="SourceSystemName" Type="Edm.String" MaxLength="255"/>
        <Property Name="SpaFeatures" Type="PropertyEnums.SpaFeatures" MaxLength="1024"/>
        <Property Name="SpaYN" Type="Edm.Boolean"/>
        <Property Name="SpecialLicenses" Type="PropertyEnums.SpecialLicenses" MaxLength="1024"/>
        <Property Name="SpecialListingConditions" Type="PropertyEnums.SpecialListingConditions" MaxLength="1024"/>
        <Property Name="StandardStatus" Type="PropertyEnums.StandardStatus" MaxLength="25"/>
        <Property Name="StateOrProvince" Type="PropertyEnums.StateOrProvince" MaxLength="2"/>
        <Property Name="StateRegion" Type="Edm.String" MaxLength="150"/>
        <Property Name="StatusChangeTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="Stories" Type="Edm.Int64" Precision="2"/>
        <Property Name="StoriesTotal" Type="Edm.Int64" Precision="3"/>
        <Property Name="StreetAdditionalInfo" Type="Edm.String" MaxLength="50"/>
        <Property Name="StreetDirPrefix" Type="PropertyEnums.StreetDirPrefix" MaxLength="15"/>
        <Property Name="StreetDirSuffix" Type="PropertyEnums.StreetDirSuffix" MaxLength="15"/>
        <Property Name="StreetName" Type="Edm.String" MaxLength="50"/>
        <Property Name="StreetNumber" Type="Edm.String" MaxLength="25"/>
        <Property Name="StreetNumberNumeric" Type="Edm.Int64" Precision="10"/>
        <Property Name="StreetSuffix" Type="PropertyEnums.StreetSuffix" MaxLength="25"/>
        <Property Name="StreetSuffixModifier" Type="Edm.String" MaxLength="25"/>
        <Property Name="StructureType" Type="PropertyEnums.StructureType" MaxLength="25"/>
        <Property Name="SubAgencyCompensation" Type="Edm.String" MaxLength="25"/>
        <Property Name="SubAgencyCompensationType" Type="PropertyEnums.SubAgencyCompensationType" MaxLength="25"/>
        <Property Name="SubdivisionName" Type="Edm.String" MaxLength="50"/>
        <Property Name="SuppliesExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="SyndicateTo" Type="PropertyEnums.SyndicateTo" MaxLength="1024"/>
        <Property Name="SyndicationRemarks" Type="Edm.String" MaxLength="4000"/>
        <Property Name="TaxAnnualAmount" Type="Edm.Double" Precision="14"/>
        <Property Name="TaxAssessedValue" Type="Edm.Int64" Precision="14"/>
        <Property Name="TaxBlock" Type="Edm.String" MaxLength="25"/>
        <Property Name="TaxBookNumber" Type="Edm.String" MaxLength="25"/>
        <Property Name="TaxLegalDescription" Type="Edm.String" MaxLength="6000"/>
        <Property Name="TaxLot" Type="Edm.String" MaxLength="25"/>
        <Property Name="TaxMapNumber" Type="Edm.String" MaxLength="25"/>
        <Property Name="TaxOtherAnnualAssessmentAmount" Type="Edm.Double" Precision="14"/>
        <Property Name="TaxParcelLetter" Type="Edm.String" MaxLength="25"/>
        <Property Name="TaxStatusCurrent" Type="PropertyEnums.TaxStatusCurrent" MaxLength="50"/>
        <Property Name="TaxTract" Type="Edm.String" MaxLength="25"/>
        <Property Name="TaxYear" Type="Edm.Int64" Precision="4"/>
        <Property Name="TenantPays" Type="PropertyEnums.TenantPays" MaxLength="1024"/>
        <Property Name="Topography" Type="Edm.String" MaxLength="255"/>
        <Property Name="TotalActualRent" Type="Edm.Double" Precision="14"/>
        <Property Name="Township" Type="Edm.String" MaxLength="50"/>
        <Property Name="TransactionBrokerCompensation" Type="Edm.String" MaxLength="25"/>
        <Property Name="TransactionBrokerCompensationType" Type="PropertyEnums.TransactionBrokerCompensationType" MaxLength="25"/>
        <Property Name="TrashExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="UnitNumber" Type="Edm.String" MaxLength="25"/>
        <Property Name="UnitsFurnished" Type="PropertyEnums.UnitsFurnished" MaxLength="25"/>
        <Property Name="UnitTypeType" Type="PropertyEnums.UnitTypeType" MaxLength="1024"/>
        <Property Name="UnparsedAddress" Type="Edm.String" MaxLength="255"/>
        <Property Name="Utilities" Type="PropertyEnums.Utilities" MaxLength="1024"/>
        <Property Name="VacancyAllowance" Type="Edm.Int64" Precision="9"/>
        <Property Name="VacancyAllowanceRate" Type="Edm.Double" Precision="5"/>
        <Property Name="Vegetation" Type="PropertyEnums.Vegetation" MaxLength="1024"/>
        <Property Name="VideosChangeTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="VideosCount" Type="Edm.Int64" Precision="2"/>
        <Property Name="View" Type="PropertyEnums.View" MaxLength="1024"/>
        <Property Name="ViewYN" Type="Edm.Boolean"/>
        <Property Name="VirtualTourURLBranded" Type="Edm.String" MaxLength="8000"/>
        <Property Name="VirtualTourURLUnbranded" Type="Edm.String" MaxLength="8000"/>
        <Property Name="WalkScore" Type="Edm.Int64" Precision="3"/>
        <Property Name="WaterBodyName" Type="Edm.String" MaxLength="50"/>
        <Property Name="WaterSewerExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="WaterSource" Type="PropertyEnums.WaterSource" MaxLength="1024"/>
        <Property Name="WaterfrontFeatures" Type="PropertyEnums.WaterfrontFeatures" MaxLength="1024"/>
        <Property Name="WaterfrontYN" Type="Edm.Boolean"/>
        <Property Name="WindowFeatures" Type="PropertyEnums.WindowFeatures" MaxLength="1024"/>
        <Property Name="WithdrawnDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="WoodedArea" Type="Edm.Double" Precision="14"/>
        <Property Name="WorkmansCompensationExpense" Type="Edm.Double" Precision="14"/>
        <Property Name="YearBuilt" Type="Edm.Int64" Precision="4"/>
        <Property Name="YearBuiltDetails" Type="Edm.String" MaxLength="1024"/>
        <Property Name="YearBuiltEffective" Type="Edm.Int64" Precision="4"/>
        <Property Name="YearBuiltSource" Type="PropertyEnums.YearBuiltSource" MaxLength="60"/>
        <Property Name="YearEstablished" Type="Edm.Int64" Precision="4"/>
        <Property Name="YearsCurrentOwner" Type="Edm.Int64" Precision="4"/>
        <Property Name="Zoning" Type="Edm.String" MaxLength="25"/>
        <Property Name="ZoningDescription" Type="Edm.String" MaxLength="255"/>
      </EntityType>
      <EntityType Name="OpenHouse">
        <Key>
          <PropertyRef Name="OpenHouseKey"/>
        </Key>
        <Property Name="BridgeModificationTimestamp" Type="Edm.DateTimeOffset" Precision="27">
          <Annotation Term="RESO.OData.Metadata.TEST"/>
        </Property>
        <Property Name="AppointmentRequiredYN" Type="Edm.Boolean"/>
        <Property Name="ListingId" Type="Edm.String" MaxLength="255"/>
        <Property Name="ListingKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="ListingKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="ModificationTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OpenHouseAttendedBy" Type="OpenHouseEnums.OpenHouseAttendedBy" MaxLength="25"/>
        <Property Name="OpenHouseDate" Type="Edm.Date" MaxLength="10"/>
        <Property Name="OpenHouseEndTime" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OpenHouseId" Type="Edm.String" MaxLength="255"/>
        <Property Name="OpenHouseKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="OpenHouseKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="OpenHouseRemarks" Type="Edm.String" MaxLength="500"/>
        <Property Name="OpenHouseStartTime" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OpenHouseStatus" Type="OpenHouseEnums.OpenHouseStatus" MaxLength="25"/>
        <Property Name="OpenHouseType" Type="OpenHouseEnums.OpenHouseType" MaxLength="25"/>
        <Property Name="OriginalEntryTimestamp" Type="Edm.DateTimeOffset" Precision="27"/>
        <Property Name="OriginatingSystemID" Type="Edm.String" MaxLength="25"/>
        <Property Name="OriginatingSystemKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="OriginatingSystemName" Type="Edm.String" MaxLength="255"/>
        <Property Name="Refreshments" Type="Edm.String" MaxLength="255"/>
        <Property Name="ShowingAgentFirstName" Type="Edm.String" MaxLength="50"/>
        <Property Name="ShowingAgentKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="ShowingAgentKeyNumeric" Type="Edm.Int64" Precision="255"/>
        <Property Name="ShowingAgentLastName" Type="Edm.String" MaxLength="50"/>
        <Property Name="ShowingAgentMlsID" Type="Edm.String" MaxLength="25"/>
        <Property Name="SourceSystemID" Type="Edm.String" MaxLength="25"/>
        <Property Name="SourceSystemKey" Type="Edm.String" MaxLength="255"/>
        <Property Name="SourceSystemName" Type="Edm.String" MaxLength="255"/>
      </EntityType>
    </Schema>
    <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="OfficeEnums">
      <EnumType Name="OfficeAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="OfficeBranchType" UnderlyingType="Edm.Int32">
        <Member Name="Main"/>
        <Member Name="Branch"/>
        <Member Name="Stand Alone"/>
      </EnumType>
      <EnumType Name="OfficeCountyOrParish" UnderlyingType="Edm.Int32"/>
      <EnumType Name="OfficeStateOrProvince" UnderlyingType="Edm.Int32">
        <Member Name="State"/>
      </EnumType>
      <EnumType Name="OfficeStatus" UnderlyingType="Edm.Int32">
        <Member Name="Active"/>
        <Member Name="Inactive"/>
      </EnumType>
      <EnumType Name="OfficeType" UnderlyingType="Edm.Int32">
        <Member Name="Real Estate"/>
        <Member Name="Appraiser"/>
      </EnumType>
      <EnumType Name="SocialMediaType" UnderlyingType="Edm.Int32"/>
      <EnumType Name="SyndicateAgentOption" UnderlyingType="Edm.Int32">
        <Member Name="No Agent"/>
        <Member Name="Allow Agent"/>
        <Member Name="Restrict Agent"/>
      </EnumType>
      <EnumType Name="SyndicateTo" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Zillow"/>
        <Member Name="Trulia"/>
        <Member Name="hotspads.com"/>
        <Member Name="nakedapartments.com"/>
      </EnumType>
    </Schema>
    <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="MemberEnums">
      <EnumType Name="MemberAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="MemberCountry" UnderlyingType="Edm.Int32">
        <Member Name="US"/>
      </EnumType>
      <EnumType Name="MemberCountyOrParish" UnderlyingType="Edm.Int32">
        <Member Name="City"/>
      </EnumType>
      <EnumType Name="MemberDesignation" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Dr."/>
        <Member Name="Prof."/>
      </EnumType>
      <EnumType Name="MemberLanguages" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="English"/>
        <Member Name="Spanish"/>
        <Member Name="French"/>
        <Member Name="German"/>
      </EnumType>
      <EnumType Name="MemberMlsSecurityClass" UnderlyingType="Edm.Int32">
        <Member Name="Top Secret"/>
        <Member Name="Secret"/>
        <Member Name="Confidential"/>
        <Member Name="Unclassified"/>
      </EnumType>
      <EnumType Name="MemberOtherPhoneType" UnderlyingType="Edm.Int32"/>
      <EnumType Name="MemberStateLicenseState" UnderlyingType="Edm.Int32"/>
      <EnumType Name="MemberStateOrProvince" UnderlyingType="Edm.Int32">
        <Member Name="State"/>
      </EnumType>
      <EnumType Name="MemberStatus" UnderlyingType="Edm.Int32">
        <Member Name="Active"/>
        <Member Name="Inactive"/>
      </EnumType>
      <EnumType Name="MemberType" UnderlyingType="Edm.Int32">
        <Member Name="Agent"/>
        <Member Name="Broker"/>
        <Member Name="Office Manager"/>
        <Member Name="Appraiser"/>
        <Member Name="Photographer"/>
        <Member Name="Assistant"/>
        <Member Name="MLO"/>
        <Member Name="Realtor"/>
        <Member Name="Association Staff"/>
        <Member Name="MLS Staff"/>
      </EnumType>
      <EnumType Name="SocialMediaType" UnderlyingType="Edm.Int32"/>
      <EnumType Name="SyndicateTo" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Zillow"/>
        <Member Name="Trulia"/>
        <Member Name="hotspads.com"/>
        <Member Name="nakedapartments.com"/>
      </EnumType>
    </Schema>
    <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="PropertyEnums">
      <EnumType Name="AboveGradeFinishedAreaSource" UnderlyingType="Edm.Int32">
        <Member Name="Agent"/>
        <Member Name="Assessor"/>
        <Member Name="Estimate"/>
      </EnumType>
      <EnumType Name="AboveGradeFinishedAreaUnits" UnderlyingType="Edm.Int32">
        <Member Name="Square Feet"/>
        <Member Name="Square Meteres"/>
        <Member Name="Acres"/>
      </EnumType>
      <EnumType Name="AccessibilityFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="Appliances" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Dishwasher"/>
        <Member Name="Disposal"/>
        <Member Name="Oven"/>
        <Member Name="Microwave"/>
        <Member Name="Pantry"/>
        <Member Name="Island"/>
      </EnumType>
      <EnumType Name="ArchitecturalStyle" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="AssociationAmenities" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Pool"/>
        <Member Name="Clubhouse"/>
        <Member Name="Gym"/>
        <Member Name="Car"/>
      </EnumType>
      <EnumType Name="AssociationFee2Frequency" UnderlyingType="Edm.Int32">
        <Member Name="Daily"/>
        <Member Name="Weekly"/>
        <Member Name="Bi-Weekly"/>
        <Member Name="Semi-Monthly"/>
        <Member Name="Monthly"/>
        <Member Name="Bi-Monthly"/>
        <Member Name="Quarterly"/>
        <Member Name="Semi-Annually"/>
        <Member Name="Annually"/>
        <Member Name="Seasonal"/>
        <Member Name="One Time"/>
      </EnumType>
      <EnumType Name="AssociationFeeFrequency" UnderlyingType="Edm.Int32">
        <Member Name="Daily"/>
        <Member Name="Weekly"/>
        <Member Name="Bi-Weekly"/>
        <Member Name="Semi-Monthly"/>
        <Member Name="Monthly"/>
        <Member Name="Bi-Monthly"/>
        <Member Name="Quarterly"/>
        <Member Name="Semi-Annually"/>
        <Member Name="Annually"/>
        <Member Name="Seasonal"/>
        <Member Name="One Time"/>
      </EnumType>
      <EnumType Name="AssociationFeeIncludes" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Cable TV"/>
        <Member Name="Earthquake Insurance"/>
        <Member Name="Electricity"/>
        <Member Name="Gas"/>
        <Member Name="Insurance"/>
        <Member Name="Maintenance Exterior"/>
        <Member Name="Maintenance Grounds"/>
        <Member Name="Pest Control"/>
        <Member Name="Security"/>
        <Member Name="Sewer"/>
        <Member Name="Snow Removal"/>
        <Member Name="Trash"/>
        <Member Name="Utilities"/>
        <Member Name="Water"/>
      </EnumType>
      <EnumType Name="Basement" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="BelowGradeFinishedAreaSource" UnderlyingType="Edm.Int32">
        <Member Name="Agent"/>
        <Member Name="Assessor"/>
        <Member Name="Estimate"/>
      </EnumType>
      <EnumType Name="BelowGradeFinishedAreaUnits" UnderlyingType="Edm.Int32">
        <Member Name="Square Feet"/>
        <Member Name="Square Meteres"/>
        <Member Name="Acres"/>
      </EnumType>
      <EnumType Name="BodyType" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="BuildingAreaSource" UnderlyingType="Edm.Int32">
        <Member Name="Agent"/>
        <Member Name="Assessor"/>
        <Member Name="Estimate"/>
      </EnumType>
      <EnumType Name="BuildingAreaUnits" UnderlyingType="Edm.Int32">
        <Member Name="Square Feet"/>
        <Member Name="Square Meteres"/>
        <Member Name="Acres"/>
      </EnumType>
      <EnumType Name="BuildingFeatures" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Concierge Service"/>
        <Member Name="Elevator"/>
        <Member Name="Cafeteria"/>
        <Member Name="Patio/Rooftop Deck"/>
        <Member Name="Gym"/>
        <Member Name="Lounge"/>
      </EnumType>
      <EnumType Name="BusinessType" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Auto Rent/Lease"/>
        <Member Name="Accounting"/>
        <Member Name="Appliances"/>
        <Member Name="Travel"/>
        <Member Name="Wholesale"/>
        <Member Name="Other (BusinessType)"/>
        <Member Name="Medical"/>
        <Member Name="Pet Store"/>
        <Member Name="Liquor Store"/>
        <Member Name="Bed &amp; Breakfast"/>
        <Member Name="Deli/Catering"/>
        <Member Name="Computer"/>
        <Member Name="Saddlery/Harness"/>
        <Member Name="Laundromat"/>
        <Member Name="Clothing"/>
        <Member Name="Retail"/>
        <Member Name="Hardware"/>
        <Member Name="Variety"/>
        <Member Name="Gas Station"/>
        <Member Name="Convalescent"/>
        <Member Name="Paints"/>
        <Member Name="Decorator"/>
        <Member Name="Photographer"/>
        <Member Name="Employment"/>
        <Member Name="Commercial"/>
        <Member Name="Books/Cards/Stationary"/>
        <Member Name="Gift Shop"/>
        <Member Name="Fitness"/>
        <Member Name="Child Care"/>
        <Member Name="Agriculture"/>
        <Member Name="Carpet/Tile"/>
        <Member Name="Cabinets"/>
        <Member Name="Warehouse"/>
        <Member Name="Home Cleaner"/>
        <Member Name="Farm"/>
        <Member Name="Financial"/>
        <Member Name="Auto Dealer"/>
        <Member Name="Athletic"/>
        <Member Name="Drugstore"/>
        <Member Name="Convenience Store"/>
        <Member Name="Franchise"/>
        <Member Name="Church"/>
        <Member Name="Florist/Nursery"/>
        <Member Name="Wallpaper"/>
        <Member Name="Manufacturing"/>
        <Member Name="Recreation"/>
        <Member Name="Residential"/>
        <Member Name="Pizza"/>
        <Member Name="Upholstery"/>
        <Member Name="Dry Cleaner"/>
      </EnumType>
      <EnumType Name="BuyerAgencyCompensationType" UnderlyingType="Edm.Int32"/>
      <EnumType Name="BuyerAgentAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="BuyerAgentDesignation" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="BuyerFinancing" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="BuyerOfficeAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="City" UnderlyingType="Edm.Int32">
        <Member Name="City"/>
      </EnumType>
      <EnumType Name="CoBuyerAgentAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="CoBuyerAgentDesignation" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="CoBuyerOfficeAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="CoListAgentAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="CoListAgentDesignation" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="CoListOfficeAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="CommonInterest" UnderlyingType="Edm.Int32"/>
      <EnumType Name="CommonWalls" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="1 Common Wall"/>
        <Member Name="2+ Common Walls"/>
        <Member Name="End Unit"/>
        <Member Name="No Common Walls"/>
        <Member Name="No One Above"/>
        <Member Name="No One Below"/>
      </EnumType>
      <EnumType Name="CommunityFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="Concessions" UnderlyingType="Edm.Int32"/>
      <EnumType Name="ConstructionMaterials" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Brick"/>
        <Member Name="Wood"/>
        <Member Name="Concrete"/>
      </EnumType>
      <EnumType Name="Cooling" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Evaporative Cooler"/>
        <Member Name="Ceiling Fan"/>
        <Member Name="Central Air"/>
        <Member Name="Room Air Conditioner"/>
      </EnumType>
      <EnumType Name="Country" UnderlyingType="Edm.Int32">
        <Member Name="US"/>
      </EnumType>
      <EnumType Name="CountyOrParish" UnderlyingType="Edm.Int32">
        <Member Name="County"/>
      </EnumType>
      <EnumType Name="CurrentFinancing" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Assumed"/>
        <Member Name="Cash"/>
        <Member Name="Contract"/>
        <Member Name="Conventional"/>
        <Member Name="FHA"/>
        <Member Name="FHA 203(b)"/>
        <Member Name="FHA 203(k)"/>
        <Member Name="Other"/>
        <Member Name="Private"/>
        <Member Name="Seller Financing"/>
        <Member Name="Trust Deed"/>
        <Member Name="USDA"/>
        <Member Name="VA"/>
      </EnumType>
      <EnumType Name="CurrentUse" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="DevelopmentStatus" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="DirectionFaces" UnderlyingType="Edm.Int32">
        <Member Name="North"/>
        <Member Name="South"/>
        <Member Name="East"/>
        <Member Name="West"/>
        <Member Name="South-West"/>
        <Member Name="North-West"/>
        <Member Name="North-East"/>
        <Member Name="South-East"/>
      </EnumType>
      <EnumType Name="Disclosures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="DistanceToBusUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToElectricUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToFreewayUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToGasUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToPhoneServiceUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToPlaceofWorshipUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToSchoolBusUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToSchoolsUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToSewerUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToShoppingUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToStreetUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DistanceToWaterUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="DocumentsAvailable" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="DoorFeatures" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="French Doors"/>
        <Member Name="Sliding Doors"/>
        <Member Name="Overhead Doors"/>
        <Member Name="Truck Doors"/>
        <Member Name="Glass Doors"/>
      </EnumType>
      <EnumType Name="Electric" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="ElementarySchool" UnderlyingType="Edm.Int32"/>
      <EnumType Name="ElementarySchoolDistrict" UnderlyingType="Edm.Int32"/>
      <EnumType Name="ElevationUnits" UnderlyingType="Edm.Int32">
        <Member Name="Feet"/>
        <Member Name="Meters"/>
      </EnumType>
      <EnumType Name="ExistingLeaseType" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="ExteriorFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="FarmLandAreaSource" UnderlyingType="Edm.Int32"/>
      <EnumType Name="FarmLandAreaUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="Fencing" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Block"/>
        <Member Name="Wrought Iron"/>
        <Member Name="Wire"/>
        <Member Name="Wood"/>
        <Member Name="Chain Link"/>
      </EnumType>
      <EnumType Name="FinancialDataSource" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Listing Broker"/>
        <Member Name="Not Available"/>
        <Member Name="Seller"/>
        <Member Name="Sellers Accountant"/>
      </EnumType>
      <EnumType Name="FireplaceFeatures" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="One"/>
        <Member Name="Living Room Fireplace"/>
        <Member Name="Wood"/>
        <Member Name="Gas"/>
        <Member Name="Two"/>
        <Member Name="Propane"/>
        <Member Name="Pellet"/>
      </EnumType>
      <EnumType Name="Flooring" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Hardwood"/>
        <Member Name="Laminate"/>
        <Member Name="Vinyl"/>
        <Member Name="Tiles"/>
        <Member Name="Cork"/>
        <Member Name="Rugs"/>
        <Member Name="Carpet"/>
      </EnumType>
      <EnumType Name="FoundationDetails" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Strip"/>
        <Member Name="Pad"/>
        <Member Name="Grillage"/>
        <Member Name="Mat"/>
        <Member Name="Pile"/>
        <Member Name="Slurry"/>
        <Member Name="Well"/>
      </EnumType>
      <EnumType Name="FrontageType" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="Furnished" UnderlyingType="Edm.Int32"/>
      <EnumType Name="GreenBuildingVerificationType" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="GreenEnergyEfficient" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="GreenEnergyGeneration" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="GreenIndoorAirQuality" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="GreenLocation" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="GreenSustainability" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="GreenWaterConservation" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="Heating" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Forced Air"/>
        <Member Name="Heat Pump"/>
        <Member Name="Boiler"/>
        <Member Name="Electric"/>
        <Member Name="Wood"/>
      </EnumType>
      <EnumType Name="HighSchool" UnderlyingType="Edm.Int32"/>
      <EnumType Name="HighSchoolDistrict" UnderlyingType="Edm.Int32"/>
      <EnumType Name="HorseAmenities" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="HoursDaysOfOperation" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="IncomeIncludes" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="InteriorFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="IrrigationSource" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="LaborInformation" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="LandLeaseAmountFrequency" UnderlyingType="Edm.Int32"/>
      <EnumType Name="LaundryFeatures" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="In Kitchen"/>
        <Member Name="Gas Dryer Hookup"/>
        <Member Name="Washer"/>
        <Member Name="Dryer"/>
      </EnumType>
      <EnumType Name="LeasableAreaUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="LeaseAmountFrequency" UnderlyingType="Edm.Int32"/>
      <EnumType Name="LeaseRenewalCompensation" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="LeaseTerm" UnderlyingType="Edm.Int32"/>
      <EnumType Name="Levels" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="One Level"/>
        <Member Name="Two Level"/>
        <Member Name="Split Level"/>
        <Member Name="Three or More Level"/>
        <Member Name="Multi Level"/>
        <Member Name="Loft"/>
      </EnumType>
      <EnumType Name="ListAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="ListAgentAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="ListAgentDesignation" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="ListOfficeAOR" UnderlyingType="Edm.Int32"/>
      <EnumType Name="ListingAgreement" UnderlyingType="Edm.Int32"/>
      <EnumType Name="ListingService" UnderlyingType="Edm.Int32">
        <Member Name="Full Service"/>
        <Member Name="Limited Service"/>
        <Member Name="Entry Only"/>
      </EnumType>
      <EnumType Name="ListingTerms" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="LivingAreaSource" UnderlyingType="Edm.Int32">
        <Member Name="Agent"/>
        <Member Name="Assessor"/>
        <Member Name="Estimate"/>
      </EnumType>
      <EnumType Name="LivingAreaUnits" UnderlyingType="Edm.Int32">
        <Member Name="SquareFeet"/>
      </EnumType>
      <EnumType Name="LockBoxType" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="LotDimensionsSource" UnderlyingType="Edm.Int32">
        <Member Name="Agent"/>
        <Member Name="Assessor"/>
        <Member Name="Estimate"/>
      </EnumType>
      <EnumType Name="LotFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="LotSizeSource" UnderlyingType="Edm.Int32">
        <Member Name="Agent"/>
        <Member Name="Assessor"/>
        <Member Name="Estimate"/>
      </EnumType>
      <EnumType Name="LotSizeUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="MLSAreaMajor" UnderlyingType="Edm.Int32"/>
      <EnumType Name="MLSAreaMinor" UnderlyingType="Edm.Int32"/>
      <EnumType Name="MajorChangeType" UnderlyingType="Edm.Int32">
        <Member Name="Price reduction"/>
        <Member Name="back on market"/>
      </EnumType>
      <EnumType Name="MiddleOrJuniorSchool" UnderlyingType="Edm.Int32"/>
      <EnumType Name="MiddleOrJuniorSchoolDistrict" UnderlyingType="Edm.Int32"/>
      <EnumType Name="MlsStatus" UnderlyingType="Edm.Int32">
        <Member Name="Active"/>
        <Member Name="Inactive"/>
      </EnumType>
      <EnumType Name="MobileDimUnits" UnderlyingType="Edm.Int32"/>
      <EnumType Name="OccupantType" UnderlyingType="Edm.Int32">
        <Member Name="Owner"/>
        <Member Name="Tenent"/>
        <Member Name="Vacant"/>
      </EnumType>
      <EnumType Name="OperatingExpenseIncludes" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="OtherEquipment" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Intercom"/>
        <Member Name="Generator"/>
        <Member Name="Central Vacuum Nozzle"/>
        <Member Name="Satellite Dish"/>
        <Member Name="TV Antenna"/>
      </EnumType>
      <EnumType Name="OtherStructures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="OwnerPays" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="OwnershipType" UnderlyingType="Edm.Int32"/>
      <EnumType Name="ParkingFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="PatioAndPorchFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="PetsAllowed" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Yes"/>
        <Member Name="No"/>
        <Member Name="Call"/>
        <Member Name="Cats OK"/>
        <Member Name="Dogs OK"/>
        <Member Name="Number Limit"/>
        <Member Name="Size Limit"/>
        <Member Name="Breed Restrictions"/>
      </EnumType>
      <EnumType Name="PoolFeatures" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Indoor Pool"/>
        <Member Name="Outdoor Pool"/>
        <Member Name="Inground Pool"/>
      </EnumType>
      <EnumType Name="Possession" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Close of Escrow"/>
        <Member Name="Close Plus 1 Day"/>
        <Member Name="Close Plus 2 Days"/>
        <Member Name="Close Plus 3 Days"/>
        <Member Name="Close Plus 3 to 5 Days"/>
        <Member Name="Close Plus 30 Days"/>
        <Member Name="Negotiable"/>
        <Member Name="Rental Agreement"/>
        <Member Name="See Remarks"/>
        <Member Name="Seller Rent Back"/>
        <Member Name="Subject to Tenant Rights"/>
      </EnumType>
      <EnumType Name="PossibleUse" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="PostalCity" UnderlyingType="Edm.Int32"/>
      <EnumType Name="PowerProductionType" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="PropertyCondition" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="PropertySubType" UnderlyingType="Edm.Int32">
        <Member Name=" ranSubType(),"/>
      </EnumType>
      <EnumType Name="PropertyType" UnderlyingType="Edm.Int32">
        <Member Name=" propertyType,"/>
      </EnumType>
      <EnumType Name="RentIncludes" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="RoadFrontageType" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="RoadResponsibility" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="City"/>
        <Member Name="County"/>
        <Member Name="Private"/>
      </EnumType>
      <EnumType Name="RoadSurfaceType" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Gravel"/>
        <Member Name="Rock"/>
        <Member Name="Dirt"/>
        <Member Name="Granite"/>
        <Member Name="Cement"/>
        <Member Name="Asphalt"/>
      </EnumType>
      <EnumType Name="Roof" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Metal"/>
        <Member Name="Gravel"/>
        <Member Name="Composite"/>
        <Member Name="Architectural Style"/>
        <Member Name="Spanish Tile"/>
      </EnumType>
      <EnumType Name="RoomType" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="SecurityFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="Sewer" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Yes Connected"/>
        <Member Name="Septic"/>
      </EnumType>
      <EnumType Name="ShowingContactType" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Agent"/>
        <Member Name="Broker"/>
        <Member Name="Seller"/>
      </EnumType>
      <EnumType Name="ShowingDays" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="ShowingRequirements" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="Skirt" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="SpaFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="SpecialLicenses" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="SpecialListingConditions" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Standard"/>
        <Member Name="REO"/>
        <Member Name="Short Sale"/>
        <Member Name="Probate"/>
        <Member Name="Auction"/>
        <Member Name="NOD"/>
      </EnumType>
      <EnumType Name="StandardStatus" UnderlyingType="Edm.Int32">
        <Member Name="Active"/>
        <Member Name="Pending"/>
        <Member Name="Closed"/>
        <Member Name="Expired"/>
      </EnumType>
      <EnumType Name="StateOrProvince" UnderlyingType="Edm.Int32">
        <Member Name="State"/>
      </EnumType>
      <EnumType Name="StreetDirPrefix" UnderlyingType="Edm.Int32"/>
      <EnumType Name="StreetDirSuffix" UnderlyingType="Edm.Int32"/>
      <EnumType Name="StreetSuffix" UnderlyingType="Edm.Int32"/>
      <EnumType Name="StructureType" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="SubAgencyCompensationType" UnderlyingType="Edm.Int32"/>
      <EnumType Name="SyndicateTo" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Zillow"/>
        <Member Name="Trulia"/>
        <Member Name="hotspads.com"/>
        <Member Name="nakedapartments.com"/>
      </EnumType>
      <EnumType Name="TaxStatusCurrent" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Assessed"/>
        <Member Name="To Be Assessed"/>
      </EnumType>
      <EnumType Name="TenantPays" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="TransactionBrokerCompensationType" UnderlyingType="Edm.Int32"/>
      <EnumType Name="UnitsFurnished" UnderlyingType="Edm.Int32"/>
      <EnumType Name="UnitTypeType" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="Utilities" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="Vegetation" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="View" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="View"/>
        <Member Name="Lake View"/>
        <Member Name="Mountain View"/>
      </EnumType>
      <EnumType Name="WaterSource" UnderlyingType="Edm.Int32" IsFlags="true">
        <Member Name="Municipal"/>
        <Member Name="Irrigation District"/>
        <Member Name="Private Utility"/>
        <Member Name="Individual Well"/>
      </EnumType>
      <EnumType Name="WaterfrontFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="WindowFeatures" UnderlyingType="Edm.Int32" IsFlags="true"/>
      <EnumType Name="YearBuiltSource" UnderlyingType="Edm.Int32">
        <Member Name="Agent"/>
        <Member Name="Assessor"/>
        <Member Name="Estimate"/>
      </EnumType>
    </Schema>
    <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="OpenHouseEnums">
      <EnumType Name="OpenHouseAttendedBy" UnderlyingType="Edm.Int32"/>
      <EnumType Name="OpenHouseStatus" UnderlyingType="Edm.Int32"/>
      <EnumType Name="OpenHouseType" UnderlyingType="Edm.Int32">
        <Member Name="Public"/>
        <Member Name="Broker"/>
        <Member Name="Office"/>
      </EnumType>
    </Schema>
    <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="Default">
      <EntityContainer Name="Container">
        <EntitySet Name="Office" EntityType="ODataService.Office"/>
        <EntitySet Name="Member" EntityType="ODataService.Member"/>
        <EntitySet Name="Property" EntityType="ODataService.Property"/>
        <EntitySet Name="OpenHouse" EntityType="ODataService.OpenHouse"/>
      </EntityContainer>
    </Schema>
    <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="RESO.OData.Metadata">
      <Term Name="StandardName" Type="Edm.String">
        <Annotation Term="Org.OData.Core.V1.Description" String="The standard name of the entity, property, enumeration, or enumeration value"/>
      </Term>
    </Schema>
  </edmx:DataServices>
</edmx:Edmx>
""")

    assert schema.namespaces[0] == 'ODataService'
