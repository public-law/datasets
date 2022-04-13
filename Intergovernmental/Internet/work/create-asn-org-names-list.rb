#!/usr/bin/env ruby


def get_org_name(asn)
  whois_data      = `whois #{asn}`.split("\n")
  org_name_record = whois_data.select{|r| r =~ /^OrgName:/}.first
  return '' if org_name_record.nil?

  org_name        = org_name_record.split(':').last.strip
end


def output_new_record(asn, name, org_name)
  puts("#{asn}\t#{name}\t#{org_name}")
end


asn_records = File.open('../all-asns.tsv').readlines
asn_records.each do |record|
  country, asn, name = record.strip.split("\t")
  next if name == '-Reserved AS-'
  
  org_name = get_org_name(asn)
  output_new_record(asn, name, org_name)
end
