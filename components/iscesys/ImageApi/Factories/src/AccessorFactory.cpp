//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2010 to the present, california institute of technology.
// all rights reserved. united states government sponsorship acknowledged.
// any commercial use must be negotiated with the office of technology transfer
// at the california institute of technology.
// 
// this software may be subject to u.s. export control laws. by accepting this
// software, the user agrees to comply with all applicable u.s. export laws and
// regulations. user has the responsibility to obtain export licenses,  or other
// export authority as may be required before exporting such information to
// foreign countries or providing access to foreign persons.
// 
// installation and use of this software is restricted by a license agreement
// between the licensee and the california institute of technology. it is the
// user's responsibility to abide by the terms of the license agreement.
//
// Author: Giangi Sacco
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#include "AccessorFactory.h"
#include "CasterFactory.h"
#include "InterleavedFactory.h"
#include "DataCaster.h"
#include "InterleavedBase.h"
#include "DataAccessor.h"
#include "DataAccessorCaster.h"
#include "DataAccessorNoCaster.h"
#include "IQByteToFloatCpxCaster.h"
using namespace std;

DataAccessor *
AccessorFactory::createAccessor(string filename, string accessMode, int size,
    int bands, int width, string interleaved, string caster)
{

  CasterFactory CF;
  InterleavedFactory IF;
  InterleavedBase * interleavedAcc = IF.createInterleaved(interleaved);
  interleavedAcc->init(filename, accessMode, size, bands, width);
  DataCaster * casterD = CF.createCaster(caster);
  return new DataAccessorCaster(interleavedAcc, casterD);
}
DataAccessor *
AccessorFactory::createAccessor(string filename, string accessMode, int size,
    int bands, int width, string interleaved, string caster, float xmi, float xmq, int iqflip)
{

  CasterFactory CF;
  InterleavedFactory IF;
  InterleavedBase * interleavedAcc = IF.createInterleaved(interleaved);
  interleavedAcc->init(filename, accessMode, size, bands, width);
  DataCaster * casterD = CF.createCaster(caster);
  ((IQByteToFloatCpxCaster *) casterD)->setXmi(xmi);
  ((IQByteToFloatCpxCaster *) casterD)->setXmq(xmq);
  ((IQByteToFloatCpxCaster *) casterD)->setIQflip(iqflip);

  return new DataAccessorCaster(interleavedAcc, casterD);

}
DataAccessor *
AccessorFactory::createAccessor(string filename, string accessMode, int size,
    int bands, int width, string interleaved)
{

  InterleavedFactory IF;
  InterleavedBase * interleavedAcc = IF.createInterleaved(interleaved);
  interleavedAcc->init(filename, accessMode, size, bands, width);
  return new DataAccessorNoCaster(interleavedAcc);
}
DataAccessor *
AccessorFactory::createAccessor(void * poly, string interleaved, int width,
    int length, int dataSize)
{
  InterleavedFactory IF;
  InterleavedBase * interleavedAcc = IF.createInterleaved(interleaved);
  interleavedAcc->init(poly);
  interleavedAcc->setLineWidth(width);
  interleavedAcc->setNumberOfLines(length);
  interleavedAcc->setBands(1);
  interleavedAcc->setDataSize(dataSize);

  return new DataAccessorNoCaster(interleavedAcc);
}

void
AccessorFactory::finalize(DataAccessor * dataAccessor)
{
  dataAccessor->finalize();
}
