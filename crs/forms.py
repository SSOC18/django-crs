from django import forms


class AccountHolder_Type_form(forms.Form):
    Individual = forms.MultipleChoiceField(PersonParty_Type_model.objects.all())
    Organisation = forms.MultipleChoiceField(OrganisationParty_Type_model.objects.all())
    AcctHolderType = forms.CharField(max_length=1000, )

class AddressFix_Type_form(forms.Form):
    Street = forms.CharField(max_length=1000, blank=True, null=True)
    BuildingIdentifier = forms.CharField(max_length=1000, blank=True, null=True)
    SuiteIdentifier = forms.CharField(max_length=1000, blank=True, null=True)
    FloorIdentifier = forms.CharField(max_length=1000, blank=True, null=True)
    DistrictName = forms.CharField(max_length=1000, blank=True, null=True)
    POB = forms.CharField(max_length=1000, blank=True, null=True)
    PostCode = forms.CharField(max_length=1000, blank=True, null=True)
    City = forms.CharField(max_length=1000, )
    CountrySubentity = forms.CharField(max_length=1000, blank=True, null=True)

class Address_Type_form(forms.Form):
    legalAddressType = forms.CharField(max_length=1000, blank=True, null=True)
    CountryCode = forms.CharField(max_length=1000, )
    AddressFix = forms.MultipleChoiceField(AddressFix_Type_model.objects.all())
    AddressFree = forms.CharField(max_length=1000, blank=True, null=True)

class BirthInfoType_form(forms.Form):
    BirthDate = forms.DateField(blank=True, null=True)
    City = forms.CharField(max_length=1000, blank=True, null=True)
    CitySubentity = forms.CharField(max_length=1000, blank=True, null=True)
    CountryInfo = forms.MultipleChoiceField(CountryInfoType_model.objects.all())

class CRS_OECD_form(forms.Form):
    version = forms.CharField(max_length=1000, blank=True, null=True)
    MessageSpec = forms.MultipleChoiceField(MessageSpec_Type_model.objects.all())
    CrsBody = forms.MultipleChoiceField(CrsBody_Type_model.objects.all())

class ControllingPerson_Type_form(forms.Form):
    Individual = forms.MultipleChoiceField(PersonParty_Type_model.objects.all())
    CtrlgPersonType = forms.CharField(max_length=1000, blank=True, null=True)

class CorrectableAccountReport_Type_form(forms.Form):
    DocSpec = forms.MultipleChoiceField(DocSpec_Type_model.objects.all())
    AccountNumber = forms.MultipleChoiceField(FIAccountNumber_Type_model.objects.all())
    AccountHolder = forms.MultipleChoiceField(AccountHolder_Type_model.objects.all())
    ControllingPerson = forms.MultipleChoiceField(ControllingPerson_Type_model.objects.all())
    AccountBalance = forms.MultipleChoiceField(MonAmnt_Type_model.objects.all())
    Payment = forms.MultipleChoiceField(Payment_Type_model.objects.all())

class CorrectableOrganisationParty_Type_form(forms.Form):
    DocSpec = forms.MultipleChoiceField(DocSpec_Type_model.objects.all())

class CorrectablePoolReport_Type_form(forms.Form):
    DocSpec = forms.MultipleChoiceField(DocSpec_Type_model.objects.all())
    AccountCount = forms.IntegerField()
    AccountPoolReportType = forms.CharField(max_length=1000, )
    PoolBalance = forms.MultipleChoiceField(MonAmnt_Type_model.objects.all())

class CountryInfoType_form(forms.Form):
    CountryCode = forms.CharField(max_length=1000, )
    FormerCountryName = forms.CharField(max_length=1000, )

class CrsBody_Type_form(forms.Form):
    ReportingFI = forms.MultipleChoiceField(CorrectableOrganisationParty_Type_model.objects.all())
    ReportingGroup = forms.MultipleChoiceField(ReportingGroupType_model.objects.all())

class DocSpec_Type_form(forms.Form):
    DocTypeIndic = forms.CharField(max_length=1000, )
    DocRefId = forms.CharField(max_length=1000, )
    CorrMessageRefId = forms.CharField(max_length=1000, blank=True, null=True)
    CorrDocRefId = forms.CharField(max_length=1000, blank=True, null=True)

class FIAccountNumber_Type_form(forms.Form):
    AcctNumberType = forms.CharField(max_length=1000, blank=True, null=True)
    UndocumentedAccount = forms.NullBooleanField(blank=True, null=True)
    ClosedAccount = forms.NullBooleanField(blank=True, null=True)
    DormantAccount = forms.NullBooleanField(blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class FirstNameType_form(forms.Form):
    xnlNameType = forms.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class LastNameType_form(forms.Form):
    xnlNameType = forms.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class MessageSpec_Type_form(forms.Form):
    SendingCompanyIN = forms.CharField(max_length=1000, blank=True, null=True)
    TransmittingCountry = forms.CharField(max_length=1000, )
    ReceivingCountry = forms.CharField(max_length=1000, )
    MessageType = forms.CharField(max_length=1000, )
    Warning = forms.CharField(max_length=1000, blank=True, null=True)
    Contact = forms.CharField(max_length=1000, blank=True, null=True)
    MessageRefId = forms.CharField(max_length=1000, )
    MessageTypeIndic = forms.CharField(max_length=1000, blank=True, null=True)
    CorrMessageRefId = forms.CharField(max_length=1000, blank=True, null=True)
    ReportingPeriod = forms.DateField()
    Timestamp = forms.DateTimeField()

class MiddleNameType_form(forms.Form):
    xnlNameType = forms.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class MonAmnt_Type_form(forms.Form):
    currCode = forms.CharField(max_length=1000, )
    valueOf_x = forms.FloatField()

class NameOrganisation_Type_form(forms.Form):
    nameType = forms.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class NamePerson_Type_form(forms.Form):
    nameType = forms.CharField(max_length=1000, blank=True, null=True)
    PrecedingTitle = forms.CharField(max_length=1000, blank=True, null=True)
    Title = forms.CharField(max_length=1000, blank=True, null=True)
    FirstName = forms.MultipleChoiceField(FirstNameType_model.objects.all())
    MiddleName = forms.MultipleChoiceField(MiddleNameType_model.objects.all())
    NamePrefix = forms.MultipleChoiceField(NamePrefixType_model.objects.all())
    LastName = forms.MultipleChoiceField(LastNameType_model.objects.all())
    GenerationIdentifier = forms.CharField(max_length=1000, blank=True, null=True)
    Suffix = forms.CharField(max_length=1000, blank=True, null=True)
    GeneralSuffix = forms.CharField(max_length=1000, blank=True, null=True)

class NamePrefixType_form(forms.Form):
    xnlNameType = forms.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class OrganisationIN_Type_form(forms.Form):
    issuedBy = forms.CharField(max_length=1000, blank=True, null=True)
    INType = forms.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class OrganisationParty_Type_form(forms.Form):
    ResCountryCode = forms.CharField(max_length=1000, blank=True, null=True)
    IN = forms.MultipleChoiceField(OrganisationIN_Type_model.objects.all())
    Name = forms.MultipleChoiceField(NameOrganisation_Type_model.objects.all())
    Address = forms.MultipleChoiceField(Address_Type_model.objects.all())

class Payment_Type_form(forms.Form):
    Type = forms.CharField(max_length=1000, )
    PaymentAmnt = forms.MultipleChoiceField(MonAmnt_Type_model.objects.all())

class PersonParty_Type_form(forms.Form):
    ResCountryCode = forms.CharField(max_length=1000, )
    TIN = forms.MultipleChoiceField(TIN_Type_model.objects.all())
    Name = forms.MultipleChoiceField(NamePerson_Type_model.objects.all())
    Address = forms.MultipleChoiceField(Address_Type_model.objects.all())
    Nationality = forms.CharField(max_length=1000, blank=True, null=True)
    BirthInfo = forms.MultipleChoiceField(BirthInfoType_model.objects.all())

class ReportingGroupType_form(forms.Form):
    Sponsor = forms.MultipleChoiceField(CorrectableOrganisationParty_Type_model.objects.all())
    Intermediary = forms.MultipleChoiceField(CorrectableOrganisationParty_Type_model.objects.all())
    AccountReport = forms.MultipleChoiceField(CorrectableAccountReport_Type_model.objects.all())
    PoolReport = forms.MultipleChoiceField(CorrectablePoolReport_Type_model.objects.all())

class TIN_Type_form(forms.Form):
    issuedBy = forms.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )
