from django.db import models


class AccountHolder_Type_model(models.Model):
    Individual = models.ForeignKey(
        "PersonParty_Type_model",
        on_delete=models.CASCADE,
        related_name="AccountHolder_Type_Individual_PersonParty_Type",
    )
    Organisation = models.ForeignKey(
        "OrganisationParty_Type_model",
        on_delete=models.CASCADE,
        related_name="AccountHolder_Type_Organisation_OrganisationParty_Type",
    )
    AcctHolderType = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AddressFix_Type_model(models.Model):
    Street = models.CharField(max_length=1000, blank=True, null=True)
    BuildingIdentifier = models.CharField(max_length=1000, blank=True, null=True)
    SuiteIdentifier = models.CharField(max_length=1000, blank=True, null=True)
    FloorIdentifier = models.CharField(max_length=1000, blank=True, null=True)
    DistrictName = models.CharField(max_length=1000, blank=True, null=True)
    POB = models.CharField(max_length=1000, blank=True, null=True)
    PostCode = models.CharField(max_length=1000, blank=True, null=True)
    City = models.CharField(max_length=1000, )
    CountrySubentity = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Address_Type_model(models.Model):
    legalAddressType = models.CharField(max_length=1000, blank=True, null=True)
    CountryCode = models.CharField(max_length=1000, )
    AddressFix = models.ForeignKey(
        "AddressFix_Type_model",
        on_delete=models.CASCADE,
        related_name="Address_Type_AddressFix_AddressFix_Type",
    )
    AddressFree = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class BirthInfoType_model(models.Model):
    BirthDate = models.DateField(blank=True, null=True)
    City = models.CharField(max_length=1000, blank=True, null=True)
    CitySubentity = models.CharField(max_length=1000, blank=True, null=True)
    CountryInfo = models.ForeignKey(
        "CountryInfoType_model",
        on_delete=models.CASCADE,
        related_name="BirthInfoType_CountryInfo_CountryInfoType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CRS_OECD_model(models.Model):
    version = models.CharField(max_length=1000, blank=True, null=True)
    MessageSpec = models.ForeignKey(
        "MessageSpec_Type_model",
        on_delete=models.CASCADE,
        related_name="CRS_OECD_MessageSpec_MessageSpec_Type",
    )
    CrsBody = models.ForeignKey(
        "CrsBody_Type_model",
        on_delete=models.CASCADE,
        related_name="CRS_OECD_CrsBody_CrsBody_Type",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ControllingPerson_Type_model(models.Model):
    Individual = models.ForeignKey(
        "PersonParty_Type_model",
        on_delete=models.CASCADE,
        related_name="ControllingPerson_Type_Individual_PersonParty_Type",
    )
    CtrlgPersonType = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CorrectableAccountReport_Type_model(models.Model):
    DocSpec = models.ForeignKey(
        "DocSpec_Type_model",
        on_delete=models.CASCADE,
        related_name="CorrectableAccountReport_Type_DocSpec_DocSpec_Type",
    )
    AccountNumber = models.ForeignKey(
        "FIAccountNumber_Type_model",
        on_delete=models.CASCADE,
        related_name="CorrectableAccountReport_Type_AccountNumber_FIAccountNumber_Type",
    )
    AccountHolder = models.ForeignKey(
        "AccountHolder_Type_model",
        on_delete=models.CASCADE,
        related_name="CorrectableAccountReport_Type_AccountHolder_AccountHolder_Type",
    )
    ControllingPerson = models.ForeignKey(
        "ControllingPerson_Type_model",
        on_delete=models.CASCADE,
        related_name="CorrectableAccountReport_Type_ControllingPerson_ControllingPerson_Type",
        blank=True, null=True,
    )
    AccountBalance = models.ForeignKey(
        "MonAmnt_Type_model",
        on_delete=models.CASCADE,
        related_name="CorrectableAccountReport_Type_AccountBalance_MonAmnt_Type",
    )
    Payment = models.ForeignKey(
        "Payment_Type_model",
        on_delete=models.CASCADE,
        related_name="CorrectableAccountReport_Type_Payment_Payment_Type",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CorrectableOrganisationParty_Type_model(models.Model):
    OrganisationParty_Type = models.ForeignKey(
        "OrganisationParty_Type_model",
        on_delete=models.CASCADE,
    )
    DocSpec = models.ForeignKey(
        "DocSpec_Type_model",
        on_delete=models.CASCADE,
        related_name="CorrectableOrganisationParty_Type_DocSpec_DocSpec_Type",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CorrectablePoolReport_Type_model(models.Model):
    DocSpec = models.ForeignKey(
        "DocSpec_Type_model",
        on_delete=models.CASCADE,
        related_name="CorrectablePoolReport_Type_DocSpec_DocSpec_Type",
    )
    AccountCount = models.IntegerField()
    AccountPoolReportType = models.CharField(max_length=1000, )
    PoolBalance = models.ForeignKey(
        "MonAmnt_Type_model",
        on_delete=models.CASCADE,
        related_name="CorrectablePoolReport_Type_PoolBalance_MonAmnt_Type",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CountryInfoType_model(models.Model):
    CountryCode = models.CharField(max_length=1000, )
    FormerCountryName = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CrsBody_Type_model(models.Model):
    ReportingFI = models.ForeignKey(
        "CorrectableOrganisationParty_Type_model",
        on_delete=models.CASCADE,
        related_name="CrsBody_Type_ReportingFI_CorrectableOrganisationParty_Type",
    )
    ReportingGroup = models.ForeignKey(
        "ReportingGroupType_model",
        on_delete=models.CASCADE,
        related_name="CrsBody_Type_ReportingGroup_ReportingGroupType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class DocSpec_Type_model(models.Model):
    DocTypeIndic = models.CharField(max_length=1000, )
    DocRefId = models.CharField(max_length=1000, )
    CorrMessageRefId = models.CharField(max_length=1000, blank=True, null=True)
    CorrDocRefId = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class FIAccountNumber_Type_model(models.Model):
    AcctNumberType = models.CharField(max_length=1000, blank=True, null=True)
    UndocumentedAccount = models.NullBooleanField(blank=True, null=True)
    ClosedAccount = models.NullBooleanField(blank=True, null=True)
    DormantAccount = models.NullBooleanField(blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class FirstNameType_model(models.Model):
    xnlNameType = models.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class LastNameType_model(models.Model):
    xnlNameType = models.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MessageSpec_Type_model(models.Model):
    SendingCompanyIN = models.CharField(max_length=1000, blank=True, null=True)
    TransmittingCountry = models.CharField(max_length=1000, )
    ReceivingCountry = models.CharField(max_length=1000, )
    MessageType = models.CharField(max_length=1000, )
    Warning = models.CharField(max_length=1000, blank=True, null=True)
    Contact = models.CharField(max_length=1000, blank=True, null=True)
    MessageRefId = models.CharField(max_length=1000, )
    MessageTypeIndic = models.CharField(max_length=1000, blank=True, null=True)
    CorrMessageRefId = models.CharField(max_length=1000, blank=True, null=True)
    ReportingPeriod = models.DateField()
    Timestamp = models.DateTimeField()

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MiddleNameType_model(models.Model):
    xnlNameType = models.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MonAmnt_Type_model(models.Model):
    currCode = models.CharField(max_length=1000, )
    valueOf_x = models.FloatField()

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NameOrganisation_Type_model(models.Model):
    nameType = models.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NamePerson_Type_model(models.Model):
    nameType = models.CharField(max_length=1000, blank=True, null=True)
    PrecedingTitle = models.CharField(max_length=1000, blank=True, null=True)
    Title = models.CharField(max_length=1000, blank=True, null=True)
    FirstName = models.ForeignKey(
        "FirstNameType_model",
        on_delete=models.CASCADE,
        related_name="NamePerson_Type_FirstName_FirstNameType",
    )
    MiddleName = models.ForeignKey(
        "MiddleNameType_model",
        on_delete=models.CASCADE,
        related_name="NamePerson_Type_MiddleName_MiddleNameType",
        blank=True, null=True,
    )
    NamePrefix = models.ForeignKey(
        "NamePrefixType_model",
        on_delete=models.CASCADE,
        related_name="NamePerson_Type_NamePrefix_NamePrefixType",
        blank=True, null=True,
    )
    LastName = models.ForeignKey(
        "LastNameType_model",
        on_delete=models.CASCADE,
        related_name="NamePerson_Type_LastName_LastNameType",
    )
    GenerationIdentifier = models.CharField(max_length=1000, blank=True, null=True)
    Suffix = models.CharField(max_length=1000, blank=True, null=True)
    GeneralSuffix = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NamePrefixType_model(models.Model):
    xnlNameType = models.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class OrganisationIN_Type_model(models.Model):
    issuedBy = models.CharField(max_length=1000, blank=True, null=True)
    INType = models.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class OrganisationParty_Type_model(models.Model):
    ResCountryCode = models.CharField(max_length=1000, blank=True, null=True)
    IN = models.ForeignKey(
        "OrganisationIN_Type_model",
        on_delete=models.CASCADE,
        related_name="OrganisationParty_Type_IN_OrganisationIN_Type",
        blank=True, null=True,
    )
    Name = models.ForeignKey(
        "NameOrganisation_Type_model",
        on_delete=models.CASCADE,
        related_name="OrganisationParty_Type_Name_NameOrganisation_Type",
    )
    Address = models.ForeignKey(
        "Address_Type_model",
        on_delete=models.CASCADE,
        related_name="OrganisationParty_Type_Address_Address_Type",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Payment_Type_model(models.Model):
    Type = models.CharField(max_length=1000, )
    PaymentAmnt = models.ForeignKey(
        "MonAmnt_Type_model",
        on_delete=models.CASCADE,
        related_name="Payment_Type_PaymentAmnt_MonAmnt_Type",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PersonParty_Type_model(models.Model):
    ResCountryCode = models.CharField(max_length=1000, )
    TIN = models.ForeignKey(
        "TIN_Type_model",
        on_delete=models.CASCADE,
        related_name="PersonParty_Type_TIN_TIN_Type",
        blank=True, null=True,
    )
    Name = models.ForeignKey(
        "NamePerson_Type_model",
        on_delete=models.CASCADE,
        related_name="PersonParty_Type_Name_NamePerson_Type",
    )
    Address = models.ForeignKey(
        "Address_Type_model",
        on_delete=models.CASCADE,
        related_name="PersonParty_Type_Address_Address_Type",
    )
    Nationality = models.CharField(max_length=1000, blank=True, null=True)
    BirthInfo = models.ForeignKey(
        "BirthInfoType_model",
        on_delete=models.CASCADE,
        related_name="PersonParty_Type_BirthInfo_BirthInfoType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ReportingGroupType_model(models.Model):
    Sponsor = models.ForeignKey(
        "CorrectableOrganisationParty_Type_model",
        on_delete=models.CASCADE,
        related_name="ReportingGroupType_Sponsor_CorrectableOrganisationParty_Type",
        blank=True, null=True,
    )
    Intermediary = models.ForeignKey(
        "CorrectableOrganisationParty_Type_model",
        on_delete=models.CASCADE,
        related_name="ReportingGroupType_Intermediary_CorrectableOrganisationParty_Type",
        blank=True, null=True,
    )
    AccountReport = models.ForeignKey(
        "CorrectableAccountReport_Type_model",
        on_delete=models.CASCADE,
        related_name="ReportingGroupType_AccountReport_CorrectableAccountReport_Type",
        blank=True, null=True,
    )
    PoolReport = models.ForeignKey(
        "CorrectablePoolReport_Type_model",
        on_delete=models.CASCADE,
        related_name="ReportingGroupType_PoolReport_CorrectablePoolReport_Type",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class TIN_Type_model(models.Model):
    issuedBy = models.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )

