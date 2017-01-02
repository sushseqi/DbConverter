# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, LargeBinary, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Alarmcontactlist(Base):
    __tablename__ = 'alarmcontactlist'

    mngrid = Column(Integer, primary_key=True, server_default=text("nextval('alarmcontactlist_mngrid_seq'::regclass)"))
    mng_name = Column(String(50))
    mng_mail = Column(String(50))
    mng_sms = Column(String(12))
    mng_region = Column(String(50))
    mng_title = Column(String(50))


class Bankoffice(Base):
    __tablename__ = 'bankoffices'

    bankofficeid = Column(Integer, primary_key=True, server_default=text("nextval('bankoffices_bankofficeid_seq'::regclass)"))
    bankid = Column(Integer, nullable=False)
    bankoffice = Column(String(50), nullable=False)
    bankofficecode = Column(String(50))


class Bank(Base):
    __tablename__ = 'banks'

    bankid = Column(Integer, primary_key=True, server_default=text("nextval('banks_bankid_seq'::regclass)"))
    bank = Column(String(50))
    uid = Column(Integer)
    createdate = Column(DateTime)
    updateuid = Column(Integer)
    updatedate = Column(DateTime)


class Barcode(Base):
    __tablename__ = 'barcode'

    ix = Column(Integer, primary_key=True, server_default=text("nextval('barcode_ix_seq'::regclass)"))
    barcode = Column(String(50), nullable=False)
    presettype = Column(Integer, nullable=False)
    presetvalue = Column(Numeric, nullable=False)
    initializedate = Column(DateTime, nullable=False)
    createdbyuserid = Column(Integer, nullable=False)
    barcodecustomerid = Column(Integer)
    supplieddate = Column(DateTime)
    fueltypeid = Column(Integer)



